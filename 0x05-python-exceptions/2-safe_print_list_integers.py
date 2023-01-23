#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    real_number = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            real_number += 1
        except (ValueError, IndexError) as e:
            if isinstance(e, ValueError):
                continue
            if isinstance(e, IndexError):
                raise e
    print("\n", end="")
    return real_number
safe_print_list_integers(["Hi",2,5,6,3,4,2,3], 10)