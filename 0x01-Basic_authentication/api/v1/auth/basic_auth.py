#!/usr/bin/env python3
"""
Basic auth's modules,
"""
import base64
import re
from .auth import Auth


class BasicAuth(Auth):
    """ Basic Authentication
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Check the base64 part of the authorization
        """
        if type(authorization_header) == str:
            pattern = r'Basic (?p<token>.+)'
            f_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')
        return None
