#!/usr/bin/python3
"""
Contains a class BaseGeometry
"""


class BaseGeometry:
    """
    A BaseGeometry class with area
    """

    def area(self):
        """
        This method is not available yet
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a value for integer
        Args:
        name: string
        value: integer
        """
        if value.__class__ != int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
