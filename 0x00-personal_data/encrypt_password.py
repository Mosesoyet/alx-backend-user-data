#!/usr/bin/env python3
""" Password module
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """ Hashes a password using random salt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
