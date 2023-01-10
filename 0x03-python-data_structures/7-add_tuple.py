#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 1:
        tuple_a = (0, 0)
    elif len(tuple_a) == 1:
        tuple_a = (tuple_a[0], 0)
    if len(tuple_b) < 1:
        tuple_b = (0, 0)
    elif len(tuple_b) == 1:
        tuple_b = (tuple_b[0], 0)
    value_1 = tuple_a[0] + tuple_b[0]
    value_2 = tuple_a[1] + tuple_b[1]
    new_tuple = (value_1, value_2)
    return new_tuple
