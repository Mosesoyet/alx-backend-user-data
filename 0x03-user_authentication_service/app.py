#!/usr/bin/env python3
""" app's module
"""
from flask import Flask, jsonify, request
from auth import Auth

AUTH = Auth()

app = Flask(__name__)
app.secrete_key = 'random-string'


@app.route('/', strict_slashes=False)
def index():
    """ The default app page
    """
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=('POST','GET'), strict_slashes=False)
def users():
    """ Register a user
    """
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        try:
            new_user = AUTH.register_user(email, password)
            return jsonify({"email": email, "message": "user created"})
        except:
            msg = jsonify({"message": "email already registered"})
            return msg, 400


if __name__ == '__main__':
    """ run flask app
    """
    app.run(host='0.0.0.0', port="5000")
