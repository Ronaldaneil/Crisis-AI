import requests
from geopy.distance import geodesic

OVERPASS_URL = "https://overpass-api.de/api/interpreter"


def nearest_shelter(latitude, longitude):

    query = f"""
    [out:json];
    (
      node(around:5000,{latitude},{longitude})["amenity"="shelter"];
      node(around:5000,{latitude},{longitude})["amenity"="hospital"];
      node(around:5000,{latitude},{longitude})["amenity"="fire_station"];
      node(around:5000,{latitude},{longitude})["amenity"="police"];
    );
    out;
    """

    try:
        response = requests.get(
            OVERPASS_URL,
            params={"data": query},
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        elements = data.get("elements", [])

        if not elements:

            navigation_url = (
                f"https://www.google.com/maps/dir/?api=1"
                f"&destination={latitude},{longitude}"
            )

            return {
                "name": "Government Emergency Shelter",
                "distance_km": 2.0,
                "latitude": latitude,
                "longitude": longitude,
                "type": "fallback",
                "navigation_url": navigation_url
            }

        nearest = None
        minimum_distance = float("inf")

        for place in elements:

            distance = geodesic(
                (latitude, longitude),
                (place["lat"], place["lon"])
            ).km

            if distance < minimum_distance:
                minimum_distance = distance
                nearest = place

        navigation_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&destination={nearest['lat']},{nearest['lon']}"
        )

        return {
            "name": nearest.get("tags", {}).get("name", "Unnamed Facility"),
            "distance_km": round(minimum_distance, 2),
            "latitude": nearest["lat"],
            "longitude": nearest["lon"],
            "type": nearest.get("tags", {}).get("amenity", "unknown"),
            "navigation_url": navigation_url
        }

    except Exception as e:

        print("OpenStreetMap Error:", e)

        navigation_url = (
            f"https://www.google.com/maps/dir/?api=1"
            f"&destination={latitude},{longitude}"
        )

        return {
            "name": "Government Emergency Shelter",
            "distance_km": 2.0,
            "latitude": latitude,
            "longitude": longitude,
            "type": "fallback",
            "navigation_url": navigation_url
        }