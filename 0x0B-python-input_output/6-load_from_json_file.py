#!/usr/bin/python3
"""
A module that contains a function that
creates an object from a json file
"""


import json


def load_from_json_file(filename):
    """
    Returns an object from a json file

    Args:
    filename (str): The name of the file to save to
    """
    with open(filename, "w") as file:
        return json.load(file)
