"""Api.py."""
import requests
import json
import logging
import random
import re
from constants import (GEOCODE_API_KEY, GOOGLE_GEOCODE_API, WIKIPEDIA_API,
                       RADIUS)


class Geocode:
    """API Geocode client class."""

    def __init__(self, **kwargs):
        """Geocode constructor."""
        self.key = kwargs.get("key", GEOCODE_API_KEY)

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

        data = json_requester(GOOGLE_GEOCODE_API, payload)

        try:
            return {
                'address': data['results'][0]["formatted_address"],
                'lat': data['results'][0]["geometry"]["location"]["lat"],
                'lng': data['results'][0]["geometry"]["location"]["lng"]
            }
        except(KeyError, TypeError) as e:
            logging.error('api.py:get_location:{}'.format(e))
            return


class Wikipedia:
    """API Wikipedia client class."""

    def get_pageid_from_gps(self, coordinate):
        """Return one pageid from latitutde & longitude.

        This methode ask 5 pageids from nearby location and select 1 randomly.
        Parameter:
            coordinate(dict)
                lat(float): ex: 46.4039137
                lng(float): ex: 2.0145255

        Return:
            int -> wikipedia idpage
        """
        payload = {
            'action': 'query',
            'format': 'json',
            'list': 'geosearch',
            'gscoord': str(coordinate['lat']) + '|' + str(coordinate['lng']),
            'gsradius': RADIUS,
            'gslimit': 5
        }
        data = json_requester(WIKIPEDIA_API, payload)
        try:
            page = random.sample(data['query']['geosearch'], 1)
            return page[0]['pageid']
        except (KeyError, IndexError, TypeError) as e:
            logging.error('api.py:get_pageid_from_location:{}'.format(e))
            return

    def get_intro_from_pageid(self, pageid):
        """Extract title & the first phrase from wikipedia pageid.

        Parameter:
            pageid(int)

        Result:
            (dict):
                "title": str -> Article title
                "intro": str -> The first phrase of the article
        """
        payload = {
            'action': 'query',
            'format': 'json',
            'prop': 'extracts',
            'pageids': pageid,
            'formatversion': 2,
            'exsentences': 10,
            'exlimit': 1,
            'explaintext': 1
        }
        data = json_requester(WIKIPEDIA_API, payload)
        try:
            title = data['query']['pages'][0]['title']
            intro = re.findall('^.*?\\.', data['query']
                               ['pages'][0]['extract'])[0]
            return {'title': title, 'intro': intro}
        except (KeyError, IndexError, TypeError) as e:
            logging.error('api.py:get_intro_from_pageid:{}'.format(e))
            return


def json_requester(url, params):
    """Request for json data.

    Parameters:
        url(str): https://abc.xyz
        params(dict): for URL parameters (see requests.get for more details.)
    """
    try:
        r = requests.get(url, params)
        r.raise_for_status()
        data = json.loads(r.text)
        return data
    except(requests.ConnectionError,
           requests.exceptions.Timeout,
           requests.exceptions.HTTPError,
           TypeError) as e:
        logging.error('api.py:json_requester:{}'.format(e))
        logging.error('URL : {}\nPARAMS : {}'.format(url, params))
        return
