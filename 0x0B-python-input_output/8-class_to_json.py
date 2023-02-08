#!/usr/bin/python3
"""
A module that contains a function to convert
objects to dictionaries
"""


def class_to_json(obj):
    """
    Converts a class object to a dictionary
    """
    return vars(obj)
