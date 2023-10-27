#!/usr/bin/python3
"""
Index view for the API.
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route("/status", methods=["GET"])
def status():
    if request.method == "GET":
        message = {"status": "OK"}
        return jsonify(message)


@app_views.route("/stats", methods=["GET"])
def stats():
    if request.method == "GET":
        resp = {}
        PLURALS = {
            "amenities": "amenities",
            "cities": "cities",
            "places": "places",
            "reviews": "reviews",
            "states": "states",
            "users": "users",
        }
        for key, value in PLURALS.items():
            count = storage.count(value)
            resp[key] = count

        # Convert the resp dictionary to a JSON-serializable format
        serializable_resp = dict(resp)

        return jsonify(serializable_resp)
