import { useState } from "react";
import axios from "axios";
import {
  ShieldAlert,
  SendHorizontal,
  Sparkles,
  Hospital,
  Navigation,
  LoaderCircle,
} from "lucide-react";

import "./App.css";
import MapView from "./MapView";

function App() {
  const [prompt, setPrompt] = useState("");
  const [loading, setLoading] = useState(false);
  const [response, setResponse] = useState(null);

  async function askAI() {
    if (!prompt.trim()) {
      alert("Please describe the emergency.");
      return;
    }

    if (!navigator.geolocation) {
      alert("Your browser does not support location.");
      return;
    }

    setLoading(true);

    navigator.geolocation.getCurrentPosition(
      async (position) => {
        try {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;

          const res = await axios.post(
            "http://127.0.0.1:8000/assist",
            {
              prompt,
              latitude,
              longitude,
            }
          );

          setResponse(res.data);
        } catch (error) {
          console.error(error);
          alert("Unable to connect to Crisis AI Backend.");
        } finally {
          setLoading(false);
        }
      },
      (error) => {
        console.error(error);
        setLoading(false);
        alert("Unable to access your location.");
      }
    );
  }

  return (
    <div className="app">
      {/* HERO */}

      <div className="hero">
        <div className="logo">
          <ShieldAlert size={44} strokeWidth={2.4} />
        </div>

        <h1>Crisis AI</h1>

        <p>Real-Time Disaster Intelligence</p>
      </div>

      {/* INPUT */}

      <div className="inputCard">
        <label>Describe your emergency</label>

        <textarea
          rows="6"
          placeholder={`Example:

• Flood near my apartment
• Fire inside my building
• Need nearest hospital
• Earthquake nearby`}
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
        />

        <button onClick={askAI}>
          {loading ? (
            <>
              <LoaderCircle className="spin" size={20} />
              Analyzing...
            </>
          ) : (
            <>
              <SendHorizontal size={20} />
              Ask Crisis AI
            </>
          )}
        </button>
      </div>

      {/* EMPTY STATE */}

      {!response && !loading && (
        <div className="card">
          <div className="cardTitle">
            <ShieldAlert size={22} />
            <h2>Welcome to Crisis AI</h2>
          </div>

          <p>
            Describe your emergency above and Crisis AI will analyze the
            situation, recommend safety actions, locate the nearest emergency
            facility, and provide navigation assistance.
          </p>
        </div>
      )}

      {/* RESPONSE */}

      {response && (
        <>
          {/* AI RESPONSE */}

          <div className="card">
            <div className="cardTitle">
              <Sparkles size={22} />

              <h2>AI Recommendation</h2>
            </div>

            <p>{response.ai_response}</p>
          </div>

          {/* SHELTER */}

          <div className="card">
            <div className="cardTitle">
              <Hospital size={22} />

              <h2>Nearest Emergency Facility</h2>
            </div>

            <div className="facility">
              <h3>{response.shelter.name}</h3>

              <span>📍 {response.shelter.distance_km} km away</span>

              <span>Category: {response.shelter.type}</span>

              <span className="badge">
                Live GPS Navigation Available
              </span>
            </div>

            <button
              className="navButton"
              onClick={() =>
                window.open(
                  response.shelter.navigation_url,
                  "_blank"
                )
              }
            >
              <Navigation size={20} />

              Open Navigation
            </button>
          </div>

          {/* LIVE MAP */}

          <MapView
            user={{
              latitude: response.latitude,
              longitude: response.longitude,
            }}
            shelter={response.shelter}
          />
        </>
      )}

      {/* FOOTER */}

      <div
        style={{
          marginTop: "40px",
          textAlign: "center",
          color: "#6B7280",
          fontSize: "14px",
        }}
      >
        Powered by FastAPI • Mozilla Otari • OpenStreetMap • React
      </div>
    </div>
  );
}

export default App;