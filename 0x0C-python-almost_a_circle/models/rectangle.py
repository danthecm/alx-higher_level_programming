#!/usr/bin/python3
"""
Contains Rectangle Model for creating rectangles
"""
from .base import Base


class Rectangle(Base):
    """
    The Rectangle class for defining rectangles
    Args:
    id (int): The id of the model
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.validate_int(width, "width")
        self.validate_underzero(width, "width", True)
        self.__width = width
        self.validate_int(height, "height")
        self. validate_underzero(height, "height", True)
        self.__height = height
        self.validate_int(x, "x")
        self.validate_underzero(x, "x")
        self.__x = x
        self.validate_int(y, "y")
        self.validate_underzero(y, "y")
        self.__y = y
        super().__init__(id)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - \
{self.width}/{self.height}"

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.validate_int(width, "width")
        self.validate_underzero(width, "width", True)
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
        self.validate_underzero(height, "height", True)
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
        self.validate_underzero(x, "x")
        self.__x = x

    @x.getter
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.validate_int(y, "y")
        self.validate_underzero(y, "y")
        self.__y = y

    @y.getter
    def y(self):
        return self.__y

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Prints a # representation of the rectangle
        """
        if self.y > 0:
            for i in range(self.y):
                print("")
        for i in range(self.__height):
            if self.x > 0:
                print(" " * self.x, end="")
            print("#" * self.__width)

    def update(self, *args):
        """
        Update the class properties with the given arguments
        """
        update_order = ["id", "width", "height", "x", "y"]
        if len(args) <= len(update_order):
            for i in range(len(args)):
                self.__setattr__(update_order[i], args[i])

    @staticmethod
    def validate_int(value, attr):
        """
        Validates that a value is a valid integer
        """
        if not (isinstance(value, int)):
            raise TypeError(f"{attr} must be an integer")

    @staticmethod
    def validate_underzero(value, attr, equal=False):
        """
        Validates if value is less than zero
        or equal to zero if equal is True
        """
        if equal:
            if value <= 0:
                raise ValueError(f"{attr} must be > 0")
        else:
            if value < 0:
                raise ValueError(f"{attr} must be >= 0")
