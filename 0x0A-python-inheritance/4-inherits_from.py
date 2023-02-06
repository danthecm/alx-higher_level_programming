#!/usr/bin/python3
"""
A module containing a function to check if two instance
are exactly of the same class, or inherits from thesame class
"""


def inherits_from(obj, a_class):
    """
    A function to check if two instances are of the same class

    Args:
    obj: instance of class
    a_class: name of class
    """
    return issubclass(obj.__class__, a_class) \
        if obj.__class__ is not a_class else False
