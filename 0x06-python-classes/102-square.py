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

    @size.setter
    def size(self, value) -> int:
        if not isinstance(value, (int)):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Returns the area of the Square
        """
        return self.__size * self.__size

    def __eq__(self, __value: object) -> bool:
        """
        Returns true if the square areas are equal else false
        """
        return isinstance(__value, Square) and self.area() == __value.area()

    def __ne__(self, __value: object) -> bool:
        """
        Returns true if the square areas are not equl else false
        """
        return isinstance(__value, Square) and self.area() != __value.area()

    def __gt__(self, __value: object) -> bool:
        """
        Returns true if the square area is greater else false
        """
        return isinstance(__value, Square) and self.area() > __value.area()

    def __lt__(self, __value: object) -> bool:
        """
        Returns true if the square area is lesser else false
        """
        return isinstance(__value, Square) and self.area() < __value.area()
