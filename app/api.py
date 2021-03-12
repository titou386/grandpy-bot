"""Api.py."""
import requests
import json
import logging
from constants import GEOCODE_API_KEY


class Geocode:
    """API Geocode client class."""

    def __init__(self, **kwargs):
        """Geocode constructor."""
        if 'key' in kwargs:
            self.key = kwargs['key']
        else:
            self.key = GEOCODE_API_KEY

    def get_location(self, place):
        """Find an address and GPS coordinates.

        parameter:
            place(lst) list of words of the place to search

        return
            dict
                address: (str) Postal address.
                lat: (float)
                lng: (float)
        """
        payload = {
            'address': ' '.join(place) + ',FR',
            'key': self.key
        }

        try:
            r = requests.get('https://maps.googleapis.com/\
maps/api/geocode/json', payload)
            r.raise_for_status()
            if r.ok:
                data = json.loads(r.text)
                if data['status'] != "OK":
                    logging.error('api.py:Geocode:get_location():status {}'
                                  .format(data['status']))
                    logging.error('api.py:Geocode:get_location():error msg {}'
                                  .format(data['error_message']))
                    return None
            else:
                logging.error('api.py:Geocode:get_location():\
HTTP error code {}'.format(r.status_code))
                return None
        except(requests.ConnectionError,
               requests.exceptions.Timeout,
               requests.exceptions.HTTPError) as e:
            logging.error('api.py:Geocode:get_location():{}'.format(e))
            return None

        return {
            'address': data['results'][0]["formatted_address"],
            'lat': data['results'][0]["geometry"]["location"]["lat"],
            'lng': data['results'][0]["geometry"]["location"]["lng"]
        }
