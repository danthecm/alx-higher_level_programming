#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) < 1:
        return None
    max_value = 0
    for integer in my_list:
        try:
            int(integer)
        except Exception as e:
            raise e
        if max_value < integer:
            max_value = integer
    return max_value
