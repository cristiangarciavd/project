"""Module for API constants
"""
from enum import Enum

class HttpMethods(Enum):
    """To manage Http Methods
    """
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
