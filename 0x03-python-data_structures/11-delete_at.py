#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    try:
        my_list = [x for index, x in enumerate(my_list) if index != idx]
    except IndexError:
        return my_list
    return my_list
