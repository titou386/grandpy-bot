"""Main.py"""
from flask import Flask, render_template, jsonify, request
from app.parser import Parser
from app.api import Geocode, Wikipedia

app = Flask(__name__)


@app.route('/')
def index():
    """Homepage."""
    return render_template("index.html")


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


if __name__ == "__main__":
    app.run(debug=True)
