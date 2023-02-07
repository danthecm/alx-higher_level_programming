#!/usr/bin/python3
"""
A module containing a class that Myint
"""


class MyInt(int):
    """MyInt is a rebel class that inherits from int. 
    The == and != operators are inverted in this class.
    """

    def __eq__(self, other):
        """Return the opposite of the result of the equality comparison of self and other."""
        return not super().__eq__(other)

    def __ne__(self, other):
        """Return the opposite of the result of the inequality comparison of self and other."""
        return not super().__ne__(other)
