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
        if path is not None and excluded_paths is not None:
            for excl_path in map(lambda x: x.strip(), excluded_paths):
                if excl_path[-1] == '*':
                    pattern = '{}/*'.format(excl_path[0:-1])
                else:
                    pattern = '{}/*'.format(excl_path)
                if re.match(pattern, path):
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
