from math import radians, sin, cos, sqrt, atan2

# Temporary shelter database
SHELTERS = [
    {
        "name": "Government School Shelter",
        "lat": 17.3850,
        "lon": 78.4867,
    },
    {
        "name": "Community Hall Shelter",
        "lat": 17.4100,
        "lon": 78.4500,
    },
    {
        "name": "District Relief Camp",
        "lat": 17.4300,
        "lon": 78.5000,
    },
]

def distance(lat1, lon1, lat2, lon2):
    R = 6371

    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1))
        * cos(radians(lat2))
        * sin(dlon / 2) ** 2
    )

    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c


def nearest_shelter(user_lat, user_lon):
    nearest = None
    best_distance = float("inf")

    for shelter in SHELTERS:
        d = distance(
            user_lat,
            user_lon,
            shelter["lat"],
            shelter["lon"],
        )

        if d < best_distance:
            best_distance = d
            nearest = shelter

    return {
        "name": nearest["name"],
        "distance_km": round(best_distance, 2),
    }