#!/usr/bin/env python3
""" The auth modules
"""
from flask import request
from typing import List, TypeVar


class Auth:
    """
    A class to implement authentication
    """


    def __init__(self):
        pass


    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check for authentication on app
        """
        return False


    def authorization_header(self, request=None) -> str:
        """ Authorization header that returns None
        """
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Check for current user info
        """
        return None
