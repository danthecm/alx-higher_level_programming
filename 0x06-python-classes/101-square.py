#!/usr/bin/python3
"""
A simple implementtation of a square class that accepts size
"""


class Square:
    """A class for generating squares

    Args:
    sizes (int): The size of the square
    """

    def __init__(self, size=0, position=(0, 0)) -> None:
        if not isinstance(size, (int)):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) < 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(
            position[0], int
        ) or not isinstance(
            position[1], int
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def __str__(self):
        """Returns a string representation of a Square"""
        str_rep = ""
        if self.size == 0:
            str_rep = ""
        else:
            for i in range(self.position[1]):
                str_rep += "\n"
            for i in range(0, self.size):
                if self.position[0] > 0:
                    str_rep += ' ' * self.position[0]
                str_rep += "#" * self.size
                str_rep += "\n" if i != self.size - 1 else ""
        return str_rep

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

    @property
    def position(self) -> tuple:
        return self.__position

    @position.setter
    def position(self, value) -> tuple:
        print("the setter position value is: {}".format(value))
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print("")
        else:
            for i in range(self.position[1]):
                print()
            for i in range(0, self.size):

                if self.position[0] > 0:
                    print(' ' * self.position[0], end="")
                print("#" * self.size)
