#!/usr/bin/python3
"""
A module that contains a function that
creates an object from a json file
"""


import json


def load_from_json_file(filename):
    """
    Creates an Object from a "JSON file".

    :param filename: The name of the file to be read and deserialized.
    :return: The object created from the JSON representation in the file.
    """
    with open(filename, "r") as file:
        return json.load(file)
