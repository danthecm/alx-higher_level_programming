#!/usr/bin/python3
"""
A module containing a student class
with first name, last name and age
"""


class Student:
    """
    A student class that is instantiated with

    first name, last name and age
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Converts the object to a dictionary
        """
        my_dict = vars(self)
        if isinstance(attrs, list):
            return {item: my_dict[item] for item in my_dict if item in attrs}
        return my_dict
