# precompute.py
import csv
from geopy.geocoders import Nominatim
import time

geolocator = Nominatim(user_agent="spa_locator")

spa_addresses = [
    "1511 Locust St, Walnut Creek, CA 94596",
    "309 E Katella Avenue, Orange, CA 92867",
    "224 Main St Seal Beach CA 90740",
    "326 Marine Ave Suite A Newport Beach CA 92662",
    "2015 Bond St, Charlottesville, VA 22901",
    # ... keep the rest of your spa addresses here ...
    "10752 N 89th pl Ste c227 Scottsdale AZ 85260",
]

with open("spas.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["address", "lat", "lon"])  # header

    for addr in spa_addresses:
        try:
            loc = geolocator.geocode(addr, timeout=10)
            if loc:
                writer.writerow([addr, loc.latitude, loc.longitude])
                print(f"✔ {addr} -> {loc.latitude}, {loc.longitude}")
            else:
                print(f"✘ Not found: {addr}")
        except Exception as e:
            print(f"⚠ Error for {addr}: {e}")
        time.sleep(1)  # respect Nominatim rate limit
