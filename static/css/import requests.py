import requests
import json

# Send an HTTP GET request to the URL
url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/4.5_week.geojson"
response = requests.get(url)
if response.status_code == 200:
   data = json.loads(response.text)

 # Access the relevant fields
generated = data["metadata"]["generated"]
api = data["metadata"]["api"]
status = data["metadata"]["status"]
count = data["metadata"]["count"]
   
print("Error:", response.status_code)

print("Generated:", generated)
print("API:", api)
print("Status:", status)
print("Count:", count)
