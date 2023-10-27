#!/usr/bin/python3
"""
create app instance of flask
"""
from api.v1.views import app_views
from flask import Flask, jsonify, make_response, render_template, url_for
from flask_cors import CORS, cross_origin
from flasgger import Swagger
from models import storage
import os
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
# global strict slash
app.url_map.strict_slashes = False

# flask running environment
host = os.getenv("HBNB_API_HOST", "0.0.0.0")
port = os.getenv("HBNB_API_PORT", 5000)

# cors setup
cors = CORS(app, resources={r"/*": {"origins": host}})

# blueprint  for the app app_views
app.register_blueprint(app_views)


# declare teardowm for page rendering
@app.teardown_appcontext
def teardown(exception):
    """
    Closes the storage.

    Args:
        exception (Exception): The exception that occurred, if any.
    """
    storage.close()


@app.errorhandler(Exception)
def handle_exception(e):
    """
    Error handling function for Flask app.

    Args:
        e: The exception that occurred

    Returns:
        A Flask response object with the error message and status code
    """
    if isinstance(e, HTTPException):
        if type(e).__name__ == "NotFound":
            e.description = "Not Found"
        message = {"error": e.description}
        code = e.code
    else:
        message = {"error": e}
        code = 500
    return make_response(jsonify(message), code)


def set_global():
    """
    Set global error handlers for all subclasses of HTTPException.

    This function registers the `handle_exception` function as the error handler for
    all subclasses of the `HTTPException` class in the application.

    Args:
        None

    Returns:
        None
    """
    # Iterate through all subclasses of HTTPException
    for classes in HTTPException.__subclasses__():
        # Register handle_exception as the error handler for each subclass
        app.register_error_handler(classes, handle_exception)


if __name__ == "__main__":
    set_global()
    app.run(host=host, port=port)
