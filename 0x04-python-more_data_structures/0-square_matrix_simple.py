#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix_squared = map(lambda x: list(map(lambda y: y ** 2, x)), matrix)
    return list(matrix_squared)
