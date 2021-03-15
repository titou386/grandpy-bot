"""Constants for 'GrandPy' application."""
import os

GEOCODE_API_KEY = os.getenv('GEOCODE_API_KEY')
GOOGLE_GEOCODE_API = 'https://maps.googleapis.com/maps/api/geocode/json'

WIKIPEDIA_API = 'https://fr.wikipedia.org/w/api.php'
RADIUS = 10000  # meters
