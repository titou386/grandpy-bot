"""Test_api.py."""
from app.api import Geocode
import requests_mock


def test_geocode_get_location_1():
    """First test geocode get location."""
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
