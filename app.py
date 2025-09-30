from flask import Flask, render_template, request, jsonify
from geopy.geocoders import Nominatim
from geopy.distance import geodesic
import csv

app = Flask(__name__)
geolocator = Nominatim(user_agent="spa_locator")

# Load spa coordinates from CSV
spa_coords = []
with open("spas.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        spa_coords.append({
            "address": row["address"],
            "lat": float(row["lat"]),
            "lon": float(row["lon"])
        })

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    user_input = request.json.get("location", "").strip()

    # If input is blank → return nothing
    if not user_input:
        return jsonify({"user": None, "spas": []})

    # Geocode the input
    user_loc = geolocator.geocode(user_input)
    if not user_loc:
        return jsonify({"user": None, "spas": []})

    user_coords = (user_loc.latitude, user_loc.longitude)

    # Calculate distances + travel times
    results = []
    for spa in spa_coords:
        spa_coords_tuple = (spa["lat"], spa["lon"])
        dist_km = geodesic(user_coords, spa_coords_tuple).km
        dist_miles = dist_km * 0.621371  # convert km → miles

        # Only include spas within 100 miles
        if dist_miles <= 100:
            est_time_min = round(dist_miles)  # simple driving estimate: 1 mile ≈ 1 min
            results.append({
                "address": spa["address"],
                "lat": spa["lat"],
                "lon": spa["lon"],
                "distance": round(dist_miles, 2),
                "travel_time": f"{est_time_min} min"
            })

    # Sort by distance
    results = sorted(results, key=lambda x: x["distance"])

    return jsonify({
        "user": {"lat": user_loc.latitude, "lon": user_loc.longitude},
        "spas": results[:10]  # return top 10 closest within 100 miles
    })

if __name__ == "__main__":
    app.run(debug=True)
