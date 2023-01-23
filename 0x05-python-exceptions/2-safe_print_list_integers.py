#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
                real_number += 1
            except ValueError:
                continue
        print("\n", end="")
    except IndexError as e:
        raise e
    return real_number
