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


my_list = MyList()
my_list.print_sorted()
my_list.append(2)
my_list.append(1)
my_list.append(10)
my_list.append(4)
my_list.print_sorted()
my_list.append(3)
my_list.print_sorted()
my_list.append("Hi")
my_list.print_sorted()
my_list.append(5)
my_list.print_sorted()
