#!/usr/bin/python3
"""
Contains base Model for creating shapes
"""
import json


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

    def to_json_string(list_dictionaries):
        """
        Returns a string representation 
        of a given list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return json.dumps([])
        return json.dumps(list_dictionaries)
