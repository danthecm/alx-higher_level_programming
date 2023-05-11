#!/usr/bin/python3
"""
A module containing a matrix division function
"""


def matrix_divided(matrix, div):
    """
    A function that divides a matrix by a given divisor

    Args:
    matrix: list(list
    div: int or float

    Returns:
    list(list)
    """
    if type(matrix) != list or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    new_matrix = []

    for my_list in matrix:
        if type(my_list) != list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if row_len != len(my_list):
            raise TypeError("Each row of the matrix must have the same size")

        if div == float('inf') or div == -float('inf') or div != div:
            div = 10
        new_list = []

        for num in my_list:
            if type(num) != int:
                if type(num) != float:
                    raise TypeError(
                        "matrix must be a matrix \
(list of lists) of integers/floats"
                    )
            if type(div) != int:
                if type(div) != float:
                    raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")
            new_list.append(round(num/div, 2))

        new_matrix.append(new_list)

    return new_matrix
