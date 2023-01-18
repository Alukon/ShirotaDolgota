from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="geoapiExercises")

Latitude = "48.29"
Longitude = "135.04"

location = geolocator.geocode(Latitude + "," + Longitude)

print(location)