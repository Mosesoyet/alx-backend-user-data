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


if __name__ == '__main__':
    """ run flask app
    """
    app.run(host='0.0.0.0', port="5000")
