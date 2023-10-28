#!/usr/bin/python3
'''city views for our api'''

from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.city import City
from models.state import State


@app_views.route('/states/<state_id>/cities',
                 methods=['GET'], strict_slashes=False)
def cities(state_id):
    """get all cities of a specific state"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    return jsonify([city.to_dict() for city in state.cities])


@app_views.route('/cities/<city_id>', methods=['GET'], strict_slashes=False)
def single_city(city_id):
    """get a specific city by id"""
    cityObj = storage.get(City, city_id)

    if not cityObj:
        abort(404)

    return jsonify(cityObj.to_dict())


@app_views.route('/cities/<city_id>', methods=['DELETE'], strict_slashes=False)
def del_city(city_id):
    """delete a specific city by id"""
    cityObj = storage.get(City, city_id)

    if not cityObj:
        abort(404)

    cityObj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states/<state_id>/cities',
                 methods=['POST'], strict_slashes=False)
def post_city(state_id):
    """create new city in the specifid state id"""
    state = storage.get(State, state_id)

    if not state:
        abort(404)

    new_city = request.get_json()
    if not new_city:
        abort(400, "Not a JSON")

    if 'name' not in new_city:
        abort(400, "Missing name")

    cityObj = City(**new_city)
    setattr(cityObj, 'state_id', state_id)
    storage.new(cityObj)
    storage.save()
    return make_response(jsonify(cityObj.to_dict()), 201)


@app_views.route('/cities/<city_id>', methods=['PUT'], strict_slashes=False)
def put_city(city_id):
    """update city object and returns it if successfull"""
    cityObj = storage.get(City, city_id)

    if not cityObj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    for k, v in req.items():
        if k not in ['id', 'created_at', 'update_at', 'state_id']:
            setattr(cityObj, k, v)

    storage.save()
    return make_response(jsonify(cityObj.to_dict()), 200)
