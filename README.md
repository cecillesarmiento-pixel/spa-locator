🧖‍♀️ Spa Finder

A simple Flask web app that helps you find the nearest spas to a given location.
It uses Geopy to geocode the user’s input, calculates distance to spas from a CSV file,
and displays results on a Leaflet map with estimated driving times.

🚀 Features

Search spas by typing a location and hitting Enter (no need to click Search).

Clears results automatically if the search box is emptied.

Shows the nearest spas (top 10) with distance and estimated travel time.

Interactive map with markers for both the user location and spas.

Auto-zoom map to fit all markers in view.

📦 Requirements

Python 3.8+

Flask

Geopy

Install dependencies with:

pip install -r requirements.txt

📂 Project Structure
spafinder/
│── app.py
│── spas.csv
│── requirements.txt
│── templates/
│    └── index.html


app.py → main Flask app

spas.csv → list of spas with addresses + coordinates

index.html → frontend (map + search)

requirements.txt → dependencies

▶️ Running the App

Open a terminal in your project folder.

Run the Flask app:

python app.py


Open your browser and go to:
👉 http://127.0.0.1:5000/

🗺️ Usage

Type a location in the search bar and press Enter.

The app will show:

Your location marker (red).

Spa markers (blue).

Distances + estimated driving times.

Clear the search box → results and markers disappear.

🛠️ Notes

Driving time is a simple estimate (assumes ~60 km/h average).

You can add more spas by editing spas.csv (must include address, lat, lon).

📜 License

This project is for personal/demo use.
