#!/usr/binenv python3
""" Auth's module
"""
import bcrypt


class Auth:
    """ The authentication class
    """
    

    def _hash_password(self, password) -> bytes:
        return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
