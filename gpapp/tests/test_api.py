"""Test_api.py."""
from gpapp.api import Geocode
from gpapp.api import Wikipedia
import requests_mock


def test_geocode_get_location_1():
    """Geocode get location test."""
    json_data = {
        "results": [
            {
                "address_components": [
                    {
                        "long_name": "3",
                        "short_name": "3",
                        "types": ["street_number"]
                    },
                    {
                        "long_name": "PLACE DU 8 MAI 1945",
                        "short_name": "PLACE DU 8 MAI 1945",
                        "types": ["route"]
                    },
                    {
                        "long_name": "La Cellette",
                        "short_name": "La Cellette",
                        "types": ["locality", "political"]
                    },
                    {
                        "long_name": "Creuse",
                        "short_name": "Creuse",
                        "types": ["administrative_area_level_2", "political"]
                    },
                    {
                        "long_name": "Nouvelle-Aquitaine",
                        "short_name": "Nouvelle-Aquitaine",
                        "types": ["administrative_area_level_1", "political"]
                    },
                    {
                        "long_name": "France",
                        "short_name": "FR",
                        "types": ["country", "political"]
                    },
                    {
                        "long_name": "23350",
                        "short_name": "23350",
                        "types": ["postal_code"]
                    }
                ],
                "formatted_address": "3 PLACE DU 8 MAI 1945, 23350 La Cellette,\
 France",
                "geometry": {
                    "location": {
                        "lat": 46.4039137,
                        "lng": 2.0145255
                    },
                    "location_type": "ROOFTOP",
                    "viewport": {
                        "northeast": {
                            "lat": 46.40526268029149,
                            "lng": 2.015874480291502
                        },
                        "southwest": {
                            "lat": 46.40256471970849,
                            "lng": 2.013176519708498
                        }
                    }
                },
                "place_id": "ChIJPfgqBmox-kcRomYv_f-TmLo",
                "plus_code": {
                    "compound_code": "C237+HR La Cellette, France",
                    "global_code": "8FR4C237+HR"
                },
                "types": ["establishment", "finance", "point_of_interest",
                          "post_office"]
            }
        ],
        "status": "OK"
    }

    with requests_mock.Mocker() as m:
        m.get('https://maps.googleapis.com/maps/api/geocode/json?\
address=la+poste,FR&key=1234567890ABCDEF', json=json_data)

        g = Geocode(key='1234567890ABCDEF')

        result = g.get_location(['la', 'poste'])
        assert result == {
            'lat': 46.4039137,
            'lng': 2.0145255,
            'address': "3 PLACE DU 8 MAI 1945, 23350 La Cellette, France"
        }


def test_get_pageid_from_gps():
    """Test for get_pageid_from_gps."""
    json_data = {
        "batchcomplete": "",
        "query": {
            "geosearch": [
                {
                    "pageid": 391364,
                    "ns": 0,
                    "title": "La Cellette (Creuse)",
                    "lat": 46.4047222222,
                    "lon": 2.015,
                    "dist": 97,
                    "primary": ""
                },
                {
                    "pageid": 5146533,
                    "ns": 0,
                    "title": "Ch\u00e2teau du Puy (Tercillat)",
                    "lat": 46.41194,
                    "lon": 2.04972,
                    "dist": 2842.2,
                    "primary": ""
                },
                {
                    "pageid": 391657,
                    "ns": 0,
                    "title": "Tercillat",
                    "lat": 46.4088888889,
                    "lon": 2.055,
                    "dist": 3152.2,
                    "primary": ""
                },
                {
                    "pageid": 12736252,
                    "ns": 0,
                    "title": "Ch\u00e2teau d'\u00c9cosse",
                    "lat": 46.3720487,
                    "lon": 2.0297435,
                    "dist": 3730.5,
                    "primary": ""
                },
                {
                    "pageid": 463677,
                    "ns": 0,
                    "title": "Sazeray",
                    "lat": 46.42889,
                    "lon": 2.053611,
                    "dist": 4085.4,
                    "primary": ""
                }
            ]
        }
    }
    with requests_mock.Mocker() as m:
        m.get('https://fr.wikipedia.org/w/api.php?action=query&format=json&\
list=geosearch&gscoord=46.4039137%7C2.0145255&gsradius=10000&gslimit=5',
              json=json_data)
        w = Wikipedia()
        pageid = w.get_pageid_from_gps({
            'lat': 46.4039137,
            'lng': 2.0145255,
            'address': "3 PLACE DU 8 MAI 1945, 23350 La Cellette, France"
        })
        assert pageid in [391364, 5146533, 391657, 12736252, 463677]


def test_get_intro_from_pageid():
    """Test for get_intro_from_pageid."""
    w = Wikipedia()
    content = w.get_intro_from_pageid(391364)
    assert content == {"title": "La Cellette (Creuse)",
                       "intro": """La Cellette est une commune française\
 située dans le département de la Creuse en région Nouvelle-Aquitaine."""}
