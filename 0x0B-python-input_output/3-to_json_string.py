#!/usr/bin/python3
"""
A module containing a function that converts an object
to a json string
"""


import json


def to_json_string(my_obj):
    """
    Converts an object to a json string

    Args:
    my_obj: The object to convert

    Returns:
    a json string representation of my_obj
    """
    return json.dumps(my_obj)
