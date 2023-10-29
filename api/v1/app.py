#!/usr/bin/python3
""" flask app for our api """
from os import getenv
from flask import Flask, jsonify
from api.v1.views import app_views
from models import storage

app = Flask(__name__)

app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.errorhandler(404)
def not_found(error):
    """ handle 404 error status """
    return jsonify({'error': 'Not found'}), 404


@app.teardown_appcontext
def teardown(exception):
    """ shutdown engine """
    storage.close()


if __name__ == '__main__':
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', 5000)
    app.run(host=host, port=port, threaded=True)
