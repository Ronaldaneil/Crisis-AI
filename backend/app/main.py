from fastapi import FastAPI
from pydantic import BaseModel

from app.security import check_prompt
from app.complexity import calculate_complexity
from app.router import select_model
from app.budget import check_budget
from app.otari import ask_otari
from app.shelter import nearest_shelter

app = FastAPI(
    title="Crisis AI Backend",
    description="AI-powered Disaster Response Assistant",
    version="1.0.0"
)


class AssistRequest(BaseModel):
    prompt: str
    latitude: float
    longitude: float


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Welcome to Crisis AI!"
    }


@app.post("/assist")
def assist(request: AssistRequest):

    # Step 1: Security Check
    safe, reason = check_prompt(request.prompt)

    if not safe:
        return {
            "status": "blocked",
            "reason": reason
        }

    # Step 2: Calculate complexity
    complexity = calculate_complexity(request.prompt)

    # Step 3: Select model
    routing = select_model(complexity)

    # Step 4: Check budget
    budget = check_budget(routing["estimated_cost"])

    if not budget["allowed"]:
        return {
            "status": "Budget Exceeded",
            "remaining_budget": budget["remaining_budget"]
        }

    # Step 5: Find nearest shelter
    shelter = nearest_shelter(
        request.latitude,
        request.longitude
    )

    # Step 6: Build contextual prompt
    context_prompt = f"""
You are Crisis AI, an intelligent disaster response assistant.

User Location:
Latitude: {request.latitude}
Longitude: {request.longitude}

Nearest Shelter:
{shelter["name"]}

Distance:
{shelter["distance_km"]} km

User Request:
{request.prompt}

Instructions:
1. Respond as a disaster response expert.
2. Mention the nearest shelter by name.
3. Mention its distance.
4. Give practical safety advice.
5. Keep the response concise and helpful.
"""

    # Step 7: Ask Otari
    ai_response = ask_otari(
        context_prompt,
        routing["model"]
    )

    # Step 8: Return response
    return {
        "status": "accepted",
        "complexity": complexity,
        "selected_model": routing["model"],
        "routing_reason": routing["reason"],
        "estimated_cost": routing["estimated_cost"],
        "remaining_budget": budget["remaining_budget"],
        "shelter": shelter,
        "ai_response": ai_response,
        "latitude": request.latitude,
        "longitude": request.longitude
    }