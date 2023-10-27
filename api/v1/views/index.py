#!/usr/bin/python3
"""
Index view for the API.
"""
from textwrap import indent
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route("/status", methods=["GET"])
def status():
    if request.method == "GET":
        message = {
            "Status": "OK"
        }
        return jsonify(message, indent=2)


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
            resp[key] = storage.count(value)
        return jsonify(resp)
