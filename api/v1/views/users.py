#!/usr/bin/python3
'''user views for our api'''
from flask import abort, jsonify, make_response, request
from api.v1.views import app_views
from models import storage
from models.user import User

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """get all users in storage"""
    userObjs = storage.all(User)
    return jsonify([obj.to_dict() for obj in userObjs.values()])

@app_views.route('/users/<user_id>', methods=['GET'], strict_slashes=False)
def get_user(user_id):
    """get a specific user by id"""
    userObj = storage.get(User, user_id)
    if not userObj:
        abort(404)
    return jsonify(userObj.to_dict())

@app_views.route('/users/<user_id>', methods=['DELETE'], strict_slashes=False)
def delete_user(user_id):
    """delete a specific user by id"""
    userObj = storage.get(User, user_id)
    if not userObj:
        abort(404)
    userObj.delete()
    storage.save()
    return make_response(jsonify({}), 200)

@app_views.route('/users', methods=['POST'], strict_slashes=False)
def create_user():
    """create user object and return it if successful"""
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    if 'email' not in data:
        abort(400, "Missing email")
    if 'password' not in data:
        abort(400, 'Missing password')
    obj = User(**data)
    storage.new(obj)
    storage.save()
    return make_response(jsonify(obj.to_dict()), 201)

@app_views.route('/users/<user_id>', methods=['PUT'], strict_slashes=False)
def update_user(user_id):
    """update user object and return it if successful"""
    userObj = storage.get(User, user_id)
    if not userObj:
        abort(404)
    data = request.get_json()
    if not data:
        abort(400, "Not a JSON")
    for k, v in data.items():
        if k not in ['id', 'email', 'created_at', 'updated_at']:
            setattr(userObj, k, v)
    storage.save()
    return make_response(jsonify(userObj.to_dict()), 200)
