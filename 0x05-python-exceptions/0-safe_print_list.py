#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for i in range(0, x):
            number += 1
            print("{}".format(my_list[i]), end="") if i - 1 != x else print("{}".format(my_list[i]))
    except Exception as e:
        number = 0
    return number
