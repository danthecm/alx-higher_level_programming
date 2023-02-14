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
        super().__init__(id, size, size, x, y)

    def __str__(self):
        message = "[Square] ({}) {}/{} - {}"
        return message.format(self.id, self.x, self.y, self.width)
