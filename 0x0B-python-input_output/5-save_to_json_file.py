#!/usr/bin/python3
"""
A module that contains a function that
converts an object to a string and writes it to a file
"""


import json


def save_to_json_file(my_obj, filename):
    my_str = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(my_str)
