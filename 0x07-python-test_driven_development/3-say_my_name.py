#!/usr/bin/python3
"""
A module containing a say_my_name function
"""


def say_my_name(first_name, last_name=""):
    """
    A function that prints first_name and last_name

    Args:
    first_name: string
    last_name (optional): string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
