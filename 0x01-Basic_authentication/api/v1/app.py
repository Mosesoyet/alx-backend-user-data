#!/usr/bin/env python3
"""
Route module for the API
"""
import json
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
from flask_cors import (CORS, cross_origin)
import os
from werkzeug.exceptions import HTTPException


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


# Define a custome error handler
@app.Errorhandler(HTTPException)
def handle_exception(e):
    """ Return an error for a  HTTP unauthorized request
    """
    response = e.get_response()
    response.data = json.dumps({
        "code": 401,
        "error": "Unauthorized"
        })
    reesponse.content_type = "application/json"
    return response

@app.errorhandler(404)
def not_found(error) -> str:
    """ Not found handler
    """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
