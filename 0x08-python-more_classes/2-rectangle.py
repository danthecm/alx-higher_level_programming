#!/usr/bin/python3
"""Contains a Simple Rectangle Class"""


class Rectangle:
    """Creates a simple Rectangle Object"""

    def __init__(self, width=0, height=0):
        "Initializes a Rectangle"
        self.validate(width, "width")
        self.__width = width
        self.validate(height, "height")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate(value, "height")
        self.__height = value

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the Rectangle"""
        return 2 * (self.__width + self.__height)

    @staticmethod
    def validate(value, word):
        """Validates a value against the following
        1: value is an integer
        2: value is greater than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(word))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(word))
