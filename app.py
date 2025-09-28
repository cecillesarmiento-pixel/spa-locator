# app.py
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
    user_input = request.json.get("location")
    user_loc = geolocator.geocode(user_input)

    if not user_loc:
        return jsonify({"error": "Location not found."}), 400

    user_coords = (user_loc.latitude, user_loc.longitude)

    # Calculate distances
    results = []
    for spa in spa_coords:
        spa_coords_tuple = (spa["lat"], spa["lon"])
        dist = geodesic(user_coords, spa_coords_tuple).km
        results.append({
            "address": spa["address"],
            "lat": spa["lat"],
            "lon": spa["lon"],
            "distance": round(dist, 2)
        })

    # Sort by distance
    results = sorted(results, key=lambda x: x["distance"])

    return jsonify({
        "user": {"lat": user_loc.latitude, "lon": user_loc.longitude},
        "spas": results[:10]
    })

if __name__ == "__main__":
    app.run(debug=True)
