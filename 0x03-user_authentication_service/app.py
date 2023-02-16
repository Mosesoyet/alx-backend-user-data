#!/usr/bin/env python3
""" app's module
"""
from flask import Flask, jsonify, request
from auth import Auth

app = Flask(__name__)
app.secrete_key = 'random-string'

AUTH = Auth()


@app.route('/', strict_slashes=False)
def index():
    """ The default app page
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users() -> str:
    """ Register a user
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"})
    except ValueError:
        return jsonify({"message": "email already registered"}), 400


if __name__ == '__main__':
    """ run flask app
    """
    app.run(host='0.0.0.0', port="5000")
