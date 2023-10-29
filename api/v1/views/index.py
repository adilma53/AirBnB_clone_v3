#!/usr/bin/python3
"""
Index view for the API.
"""
from api.v1.views import app_views
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User



@app_views.route("/status", strict_slashes=False, methods=["GET"])
def status():
    """
    Handler function for the /status endpoint.

    Returns:
        A JSON response with the status "OK".
    """
    return {
        "status": "OK",
    }


@app_views.route("/stats", strict_slashes=False, methods=["GET"])
def stats():
    amenities = storage.count(Amenity)
    cities = storage.count(City)
    places = storage.count(Place)
    reviews = storage.count(Review)
    states = storage.count(State)
    users = storage.count(User)
    return {
        "amenities": amenities,
        "cities": cities,
        "places": places,
        "reviews": reviews,
        "states": states,
        "users": users,
    }


if __name__ == "__main__":
    pass
