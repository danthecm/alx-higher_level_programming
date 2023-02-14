#!/usr/bin/python3
"""
Contains base Model for creating shapes
"""


class Base:
    """
    The base class from which all other models are created

    Args:
    id (int): The id of the model
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if not id:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
