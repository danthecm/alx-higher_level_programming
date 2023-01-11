#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    try:
        list_index = [index for index, x in enumerate(my_list) if index == idx]
        my_list.remove(my_list[list_index[0]])
    except IndexError:
        return my_list
    return my_list
