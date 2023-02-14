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
        self.width = width
        self.height = height
        self.y = y
        self.x = x

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validate_int(width, "width")
        self.__width = width

    @width.getter
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.validate_int(height, "height")
        self.__height = height

    @height.getter
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        self.validate_int(x, "x")
        self.__x = x

    @width.getter
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validate_int(y, "y")
        self.__y = y

    @y.getter
    def y(self):
        return self.__y

    @staticmethod
    def validate_int(value, attr):
        """
        Validates that a value is a valid integer
        """
        if not (isinstance(value, int)):
            raise TypeError(f"{attr} must be an integer")


r1 = Rectangle(10, 2)
print(r1.id)

r2 = Rectangle(2, 10)
print(r2.id)

r3 = Rectangle(10, 2, 0, 0, 12)
print(r3.id)
