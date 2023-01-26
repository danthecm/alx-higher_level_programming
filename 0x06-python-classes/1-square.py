#!/usr/bin/python3
"""
A simple implementtation of a square class that accepts size
"""


class Square:
    """A class for generating squares

    Args:
    sizes (int): The size of the square
    """

    def __init__(self, size) -> None:
        self.__size = size
