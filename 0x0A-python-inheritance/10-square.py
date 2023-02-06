#!/usr/bin/python3
"""
Contains a class Rectangle class
"""
BaseGeometry = __import__("9-base_geometry").Rectangle


class Square(BaseGeometry):
    """
    A Rectangle class based on the base geometry class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
