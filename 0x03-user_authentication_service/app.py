#!/usr/bin/python3
""" app's module
"""
from flask import Flask, jsonify

app = Flask(__name__)
app.secrete_key = 'random-string'


@app.route('/', strict_slashes=False)
def index():
    """ The default app page
    """
    return jsonify({"message": "Bienvenue"})
