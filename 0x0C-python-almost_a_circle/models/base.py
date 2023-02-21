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

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of object to a json file
        """
        if list_objs is None or len(list_objs) < 1:
            with open(f"{cls.__name__}.json", "w", encoding="utf8") as f:
                f.write(cls.to_json_string(list_objs))
        else:
            with open(f"{cls.__name__}.json", "w", encoding="utf8") as f:
                f.write(cls.to_json_string(
                    [item.to_dictionary() for item in list_objs]))

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns a string representation
        of a given list of dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) < 1:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list representation
        of a given json string
        """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns an instance of the class
        with all attributes set
        """
        dummy_class = cls(1, 1, 1)
        dummy_class.update(**dictionary)
        return dummy_class
