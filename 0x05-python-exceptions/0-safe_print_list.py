#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    number = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            number += 1
    except Exception as e:
        pass
    print("\n", end="")
    return number
