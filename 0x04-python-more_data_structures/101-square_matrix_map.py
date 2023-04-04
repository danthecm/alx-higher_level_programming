#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(square_matrix, matrix))


def square_matrix(matrix):
    return list(map(square_list, matrix))


def square_list(item):
    return item * item
