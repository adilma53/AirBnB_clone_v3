#!/usr/bin/python3
'''user views for our api'''

from flask import jsonify, abort, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.get('/users')
def get_users():
    """get all users in storage"""

    users = [
        user.to_dict()
        for user in storage.all(User).values()
    ]

    return jsonify(users)


@app_views.get('/users/<user_id>')
def get_user(user_id):
    """get a specific user by id"""

    user = storage.get(User, user_id)

    if user:
        return jsonify(user.to_dict())

    abort(404)


@app_views.delete('/users/<user_id>')
def delete_user(user_id):
    """delete a specific user by id"""

    user = storage.get(User, user_id)

    if user:
        storage.delete(user)
        storage.save()
        return jsonify({})

    abort(404)


@app_views.post('/users')
def post_user():
    """create user object and return it if successfull"""

    body = request.get_json()
    if not body:
        abort(400, 'Not a JSON')
    if 'email' not in body:
        abort(400, 'Missing email')
    if 'password' not in body:
        abort(400, 'Missing password')
    user = User(**body)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.put('/users/<user_id>')
def put_user(user_id):
    """update user object and return it if successfull"""
    user = storage.get(User, user_id)

    if not user:
        abort(404)
    body = request.get_json()
    if not body:
        abort(400, 'Not a JSON')
    ignore_keys = ['id', 'email', 'created_at', 'updated_at']
    for k, v in body.items():
        if k not in ignore_keys:
            setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict())
