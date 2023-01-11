#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_list.sort()
    return sum([x for index, x in enumerate(my_list) if my_list[index - 1] != x])
