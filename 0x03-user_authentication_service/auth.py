#!/usr/binenv python3
""" Auth's module
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """ Hashes password using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
