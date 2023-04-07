#!/usr/bin/python3
"""
Magic Calculation Class based on bytecode
"""

import math


class MagicClass:
    """
    Magic Class that does some basic calculations
    """

    def __init__(self, radius) -> None:
        self.__radius = 0

        if type(radius) != int or type(radius) != float:
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Calculate the area of the circle"""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Calculate the circumference of the circle"""
        return 2 * math.pi * self.__radius
