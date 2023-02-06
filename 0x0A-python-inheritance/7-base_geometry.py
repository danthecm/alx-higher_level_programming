#!/usr/bin/python3
"""
Contains a class BaseGeometry
"""


class BaseGeometry:
    """
    A BaseGeometry class with area
    """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(name, str):
            raise TypeError("<name> must be a string")
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        elif value <= 0:
            raise ValueError("<name> must be greater than 0")
