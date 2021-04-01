# grandpy-bot
GrandPy Bot, tell us an anectdote ...

## Description
GrandPy Bot informs you about the place you are looking for

For each request, you will have as an answer:
- An address
- A map
- A short story of GrandPy bot

## Requirements
- Linux
- Python 3
- Flask
- Geocode API key
- Google Maps API key
- Flask in debug mode or webserver

## Installation
Download the repository:

    $ https://github.com/titou386/grandpy-bot.git
    $ pip install -r requirements

## Usage

Configure your environment and execute main.py:

    $ export GEOCODING_API_KEY='YOUR_GEOCODE_API_KEY'
    $ export MAPS_API_KEY='YOUR_GEOCODE_API_KEY'
    $ export FLASK_ENV=development
    $ cd grandpy-bot
    $ python3 main.py
