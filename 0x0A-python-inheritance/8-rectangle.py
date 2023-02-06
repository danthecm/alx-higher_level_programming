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
        if name.__class__ is not str:
            raise TypeError("name must be a string")
        if value.__class__ is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A Rectangle class based on the base geometry class
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
