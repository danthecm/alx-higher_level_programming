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

    def to_json(self):
        """
        Converts the object to a dictionary
        """
        return vars(self)
