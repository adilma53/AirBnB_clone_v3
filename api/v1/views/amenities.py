#!/usr/bin/python3
'''amenity views for our api'''
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities', methods=['GET'], strict_slashes=False)
def amenities():
    """get all amenities in storage"""
    amenityObjs = storage.all(Amenity)
    return jsonify([obj.to_dict() for obj in amenityObjs.values()])


@app_views.route('/amenities/<amenity_id>',
                 methods=['GET'], strict_slashes=False)
def single_amenities(amenity_id):
    """get a specific amenity by id"""
    amenityObj = storage.get(Amenity, amenity_id)
    if not amenityObj:
        abort(404)
    return jsonify(amenityObj.to_dict())


@app_views.route('/amenities/<amenity_id>',
                 methods=['DELETE'], strict_slashes=False)
def del_amenities(amenity_id):
    """delete a specific amenity by id"""
    amenityObj = storage.get(Amenity, amenity_id)
    if not amenityObj:
        abort(404)

    amenityObj.delete()
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """create amenity object and return it if successfull"""
    newObj = request.get_json()
    if not newObj:
        abort(400, "Not a JSON")
    if 'name' not in newObj:
        abort(400, "Missing name")

    obj = Amenity(**newObj)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)


@app_views.route('/amenities/<amenity_id>',
                 methods=['PUT'], strict_slashes=False)
def put_amenity(amenity_id):
    """update amenity object and return it if successfull"""
    amenityObj = storage.get(Amenity, amenity_id)
    if not amenityObj:
        abort(404)

    req = request.get_json()
    if not req:
        abort(400, "Not a JSON")

    for k, v in req.items():
        if k not in ['id', 'created_at', 'update_at']:
            setattr(amenityObj, k, v)

    storage.save()
    return make_response(jsonify(amenityObj.to_dict()), 200)
