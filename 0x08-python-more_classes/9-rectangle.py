#!/usr/bin/python3
"""Contains a Simple Rectangle Class"""


class Rectangle:
    """Creates a simple Rectangle Object"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes a Rectangle"""
        self.validate(width, "width")
        self.__width = width
        self.validate(height, "height")
        self.__height = height
        self.increament_counter()
        self.print_symbol = "#"

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""
        single_row = self.print_symbol * self.__width
        my_string = (str(single_row) + "\n") * (int(self.__height) - 1)
        my_string = my_string + str(single_row)
        return my_string

    def __repr__(self):
        return f"Rectangle({self.__width},{self.__height})"

    def __del__(self):
        print("Bye rectangle...")
        self.decreament_counter()

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate(value, "width")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate(value, "height")
        self.__height = value

    def area(self):
        """Calculates the area of the Rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Calculates the perimeter of the Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__width + self.__height)

    @classmethod
    def increament_counter(cls):
        """Increment the number of instance counter"""
        cls.number_of_instances += 1

    @classmethod
    def decreament_counter(cls):
        """Decrement the number of instance counter"""
        cls.number_of_instances -= 1

    @classmethod
    def square(cls, size=0):
        """
        Creates a square rectangle object with equal width and height
        Args:
        size (int, optional): size of the square rectangle, default is 0.
        Returns:
        Rectangle: square rectangle object with equal width and height.
        """
        cls.validate(size, "size")
        return cls(size, size)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the biggest rectangle
        Args:
        rect_1: Reactangle
        rect_2: Rectangle
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() == rect_2.area():
            return rect_1
        return rect_1 if rect_1.area() > rect_2.area() else rect_2

    @staticmethod
    def validate(value, word):
        """Validates a value against the following
        1: value is an integer
        2: value is greater than or equal to zero
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(word))
        elif value < 0:
            raise ValueError("{} must be >= 0".format(word))


my_square = Rectangle.square(19)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
