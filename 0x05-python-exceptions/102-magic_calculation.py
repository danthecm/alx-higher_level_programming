#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        if a > i:
            result += a ** b / i
            # raise Exception("Too far")
        else:
            result = a + b
    return result
