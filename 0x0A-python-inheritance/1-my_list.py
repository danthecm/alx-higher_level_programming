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
        try:
            sorted_list = self.copy()
            sorted_list.sort()
        except Exception:
            sorted_list = self.copy()
        print(sorted_list)
