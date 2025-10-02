import googlemaps

# Replace with your actual API key
gmaps = googlemaps.Client(key='YOUR_API_KEY')

# Geocode the Taj Mahal
address = "Taj Mahal, Agra, India"
geocode_result = gmaps.geocode(address)

if geocode_result:
    location = geocode_result[0]['geometry']['location']
    print(f"Latitude: {location['lat']}, Longitude: {location['lng']}")
else:
    print("Geocoding failed.")