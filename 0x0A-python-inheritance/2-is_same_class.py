#!/usr/bin/python3
"""
A module containing a function to check if two instance
are exactly of the same class
"""


def is_same_class(obj, a_class):
    """
    A function to check if two instances are of the same class

    Args:
    obj: instance of class
    a_class: name of class
    """
    return obj.__class__.__name__ == a_class.__name__
