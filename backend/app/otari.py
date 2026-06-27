import os
from pathlib import Path

from dotenv import load_dotenv
from otari import OtariClient

# Load .env file
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(env_path)

# Get API Key
API_KEY = os.getenv("OTARI_API_KEY")


def ask_otari(prompt: str, model: str):

    client = OtariClient(
        platform_token=API_KEY,
    )

    response = client.completion(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
    )

    return response.choices[0].message.content