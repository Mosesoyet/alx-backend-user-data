#!/usr/bin/env python3
""" Auth's module
"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """ Hashes password using bcrypt
    """
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


class Auth:
    """ Auth class to interract with the database
    """


    def __init__(self):
        """ Initializes a new instance of databse
        """
        self._db = DB()


    def register_user(self, email: str, password: str) -> User:
        """ Adds a new user to the database
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f'User {email} already exists')
        except NoResultFound:
            new_user = self._db.add_user(email, _hash_password(password))
            return new_user
