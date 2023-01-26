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
        self.__size = size

    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, value) -> int:
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(0, self.size):
                print("#" * self.size)
