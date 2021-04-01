"""Views.py."""
from flask import Flask, render_template, jsonify, request
from gpapp.parser import Parser
from gpapp.api import Geocode, Wikipedia


app = Flask(__name__)

app.config.from_object('constants')


@app.route('/')
def index():
    """Homepage."""
    return render_template("index.html",
                           maps_api_url=app.config['MAPS_API_URL'],
                           maps_api_key=app.config['MAPS_API_KEY']
                           )


@app.route("/search", methods=["POST"])
def search():
    """Location search page."""
    p = Parser()
    geocode = Geocode()
    wiki = Wikipedia()

    query = request.form["query"]
    location_requested = p.find_location(query)
    if location_requested:
        physical_location = geocode.get_location(location_requested)
        if physical_location:
            pageid = wiki.get_pageid_from_gps(physical_location)
            if pageid:
                content_page = wiki.get_intro_from_pageid(pageid)
                if content_page:
                    physical_location.update(content_page)
                return jsonify(physical_location)
            else:
                return jsonify(physical_location)

    return jsonify(None)
