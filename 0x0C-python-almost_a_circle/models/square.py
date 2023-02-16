#!/usr/bin/python3
"""
Contains Square Model for creating rectangles
"""
from .rectangle import Rectangle


class Square(Rectangle):
    """
    The Square class for defining squares
    Args:
    id (int): The id of the model
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        message = "[Square] ({}) {}/{} - {}"
        return message.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    @size.getter
    def size(self):
        return self.width

    def area(self):
        """
        Returns the area of the square
        """
        return super().area()

    def display(self):
        """
        Prints # representing the square
        """
        return super().display()

    def update(self, *args, **kwargs):
        """
        Update the square attributes dynamically
        """
        return super().update(*args, **kwargs)
