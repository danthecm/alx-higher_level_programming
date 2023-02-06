#!/usr/bin/python3
"""
A module containing a function to check if two instance
are exactly of the same class, or inherits from thesame class
"""


def is_kind_of_class(obj, a_class):
    """
    A function to check if two instances are of the same class

    Args:
    obj: instance of class
    a_class: name of class
    """
    return isinstance(obj, a_class) or issubclass(obj.__class__, a_class)
