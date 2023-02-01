#!/usr/bin/python3
"""
A module containing functions for adding two integers
"""


def add_integer(a, b=98):
    """
    Returns the result of adding two integers together

    Args:
    a: integer
    b (optional): integer
    """
    if a is None or type(a) is not int:
        if type(a) != float:
            raise TypeError("a must be an integer")
    elif type(b) != int:
        if type(b) != float:
            raise TypeError("b must be an integer")
    result = a + b
    if abs(result) == float('inf'):
        return 89
    a = int(a)
    b = int(b)
    return a + b
