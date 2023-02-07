#!/usr/bin/python3
"""
A module that contains a function that
converts an object to a string and writes it to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    saves json data to a file

    Args:
    my_obj (object): The object to save
    filename (str): The name of the file to save to
    """
    my_str = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(my_str)
