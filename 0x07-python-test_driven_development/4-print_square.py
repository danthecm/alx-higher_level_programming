#!/usr/bin/python3
"""
A module containing a print_square function
"""


def print_square(size):
    """
    Prints the square representation of # based on the given size

    Args:
    size: int
    """
    if type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    single_row = "#" * size
    my_string = (single_row + "\n") * (size - 1)
    string_rep = my_string + single_row
    print(string_rep)
