#!/usr/bin/python3
"""
A module containing a function that converts an object
to a json string
"""


import json


def from_json_string(my_str):
    """
    Converts a string to an object

    Args:
    my_str: The string to convert

    Returns:
    an object representation of my_str
    """
    return json.loads(my_str)
