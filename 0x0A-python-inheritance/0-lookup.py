#!/usr/bin/python3
"""
Lookup module containing a lookup function
"""


def lookup(obj):
    """
    Lookup function that returns all the attributes in the given class

    Args:
    obj: Class object
    """
    my_attributes = dir(obj)
    return my_attributes
