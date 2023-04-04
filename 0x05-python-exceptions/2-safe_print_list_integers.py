#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for i in range(0, x):
        try:
            if type(my_list[i]) != int:
                continue
            print("{:d}".format(my_list[i]), end="")
            real_number += 1
        except Exception as e:
            raise e
    print("\n", end="")
    return real_number
