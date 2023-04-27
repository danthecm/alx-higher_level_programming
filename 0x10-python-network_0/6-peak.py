#!/usr/bin/python3
"""
Contains function that finds the peak of a list of integer
"""


def find_peak(list_of_integers):
    """
    Finds the peak of a list of integers
    Args:
    list: list_of_integers
    Returns:
    int: peak if list is not empty else None
    """
    if len(list_of_integers) > 0:
        list_of_integers.sort(reverse=True)
        return list_of_integers[1]
    return None
