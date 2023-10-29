#!/usr/bin/python3
"""
Index view for the API.
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


hbnb_class = {
    "amenities": "amenities",
    "cities": "cities",
    "places": "places",
    "reviews": "reviews",
    "states": "states",
    "users": "users",
}


@app_views.route("/status", methods=["GET"])
def status():
    """
    Handler function for the /status endpoint.

    Returns:
        A JSON response with the status "OK".
    """
    if request.method == "GET":
        return jsonify({"status": "OK"})


@app_views.route("/stats", methods=["GET"])
def stats():
    """Endpoint to get statistics of the API."""
    if request.method == "GET":
        resp = {}
        for key, value in hbnb_class.items():
            resp[key] = storage.count(value)
        return jsonify(resp)


if __name__ == "__main__":
    pass
