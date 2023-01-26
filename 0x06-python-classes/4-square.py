#!/usr/bin/python3
"""
A simple implementtation of a square class that accepts size
"""


class Square:
    """A class for generating squares

    Args:
    sizes (int): The size of the square
    """

    def __init__(self, size=0) -> None:
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size

    def area(self):
        return self.__size * self.__size
