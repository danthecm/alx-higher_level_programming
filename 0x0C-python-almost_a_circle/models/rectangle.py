#!/usr/bin/python3
"""
Contains Rectangle Model for creating rectangles
"""
from base import Base


class Rectangle(Base):
    """
    The Rectangle class for defining rectangles
    Args:
    id (int): The id of the model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id=id)
        self.__width = width
        self.__height = height
        self.__y = y
        self.__x = x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @width.getter
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height

    @height.getter
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.__x = x

    @width.getter
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def y(self, y):
        self.__y = y

    @width.getter
    def y(self):
        return self.__y
