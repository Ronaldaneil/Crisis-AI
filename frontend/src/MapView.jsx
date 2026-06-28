import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

delete L.Icon.Default.prototype._getIconUrl;

L.Icon.Default.mergeOptions({
  iconRetinaUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon-2x.png",
  iconUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png",
  shadowUrl:
    "https://unpkg.com/leaflet@1.9.4/dist/images/marker-shadow.png",
});

function MapView({ user, shelter }) {
  if (!user || !shelter) return null;

  return (
    <div className="card">

      <div className="cardTitle">

        <h2>🗺 Live Emergency Map</h2>

      </div>

      <MapContainer
        center={[user.latitude, user.longitude]}
        zoom={14}
        style={{
          height: "420px",
          width: "100%",
          borderRadius: "20px",
        }}
      >
        <TileLayer
          attribution='&copy; OpenStreetMap contributors'
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        />

        {/* User */}

        <Marker
          position={[user.latitude, user.longitude]}
        >
          <Popup>

            📍 Your Current Location

          </Popup>
        </Marker>

        {/* Shelter */}

        <Marker
          position={[
            shelter.latitude,
            shelter.longitude,
          ]}
        >
          <Popup>

            <b>{shelter.name}</b>

            <br />

            {shelter.distance_km} km away

          </Popup>
        </Marker>
      </MapContainer>

    </div>
  );
}

export default MapView;