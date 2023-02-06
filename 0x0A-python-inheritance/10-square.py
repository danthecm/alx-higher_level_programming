#!/usr/bin/python3
"""
Contains a class Rectangle class
"""
BaseGeometry = __import__("9-base_geometry").Rectangle


class Square(BaseGeometry):
    """
    A Rectangle class based on the base geometry class
    """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        return self.__width * self.__height
