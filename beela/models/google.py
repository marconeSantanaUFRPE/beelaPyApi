
import googlemaps
import time
from GoogleMapsAPI import get_my_key



key = "AIzaSyBRtX18zX0geqWmzSgL7MmwSeZXeGvpoG0"


API_KEY = get_my_key()

gmaps = googlemaps.Client(key= API_KEY)

places_result = gmaps.places_nearby(location = "-8.189868, -34.954734", radius = 40000, open_now = False)

print(places_result)