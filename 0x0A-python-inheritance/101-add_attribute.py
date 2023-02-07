#!/usr/bin/python3
"""
A module containing a function to add attributes to a class
"""


def add_attribute(obj, attr_name, attr_value):
    """Add a new attribute to an object.

    Args:
    obj (object): The object to add the attribute to.
    attr_name (str): The name of the attribute to add.
    attr_value: The value of the attribute to add.

    Raises:
    TypeError: If the object can't have new attributes added to it.

    """
    if not hasattr(obj, '__setattr__'):
        raise TypeError("can't add new attribute")
    elif hasattr(obj, f"__{attr_name}"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
