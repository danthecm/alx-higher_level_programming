#!/usr/bin/python3
"""
Contains a class Square class
"""
Rectangle = __import__("9-rectangles").Rectangle


class Square(Rectangle):
    """
    A Square class based on the rectangle class
    """

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)

    def area(self):
        return self.__size * self.__size
