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

Write your Google maps API key in base.html

Execute main.py in purbeurre folder:

    $ export GEOCODE_API_KEY='YOUR_GEOCODE_API_KEY'
    $ python3 main.py
