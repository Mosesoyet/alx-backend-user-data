#!/usr/bin/env python3
""" The auth modules
"""
from flask import request
from typing import List, TypeVar
import re


class Auth:
    """
    A class to implement authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Check for authentication on app
        """
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True

        if path[-1] != '/':
            path += '/'

        if path in excluded_paths:
            return False

        return True


    def authorization_header(self, request=None) -> str:
        """ Authorization header that returns None
        """
        if request is not None:
            return request.headers.get('Authorization', None)
        return None


    def current_user(self, request=None) -> TypeVar('User'):
        """ Check for current user info
        """
        return None
