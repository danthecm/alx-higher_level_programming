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
    if type(a) != int:
        if type(a) != float:
            raise TypeError("a must be an integer")
        a = int(a)
    elif type(b) != int:
        if type(b) != float:
            raise TypeError("b must be an integer")
        b = int(b)
    elif abs(a) == float('inf') or abs(b) == float('inf'):
        raise OverflowError()
    return a + b
