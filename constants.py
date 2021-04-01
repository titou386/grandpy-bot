"""Constants for 'GrandPy' application."""
import os

GEOCODING_API_KEY = os.getenv('GEOCODING_API_KEY')
MAPS_API_KEY = os.getenv('MAPS_API_KEY')


GEOCODING_API_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MAPS_API_URL = "https://maps.googleapis.com/maps/api/js"

WIKIPEDIA_API_URL = 'https://fr.wikipedia.org/w/api.php'
RADIUS = 10000  # meters
