#!/usr/bin/python3
"""
A module that contains a custom class MyList
inheriting from the python list class
"""


class MyList(list):
    """
    A custom class that inherits from python list class

    Args:
    list: A list
    """

    def print_sorted(self):
        sorted_list = self.copy()
        sorted_list.sort()
        print(sorted_list)
