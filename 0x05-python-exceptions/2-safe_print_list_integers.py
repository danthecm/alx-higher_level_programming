#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        for i in range(0, x):
            try:
                print("{:d}".format(my_list[i]), end="")
            except ValueError as e:
                pass
        print("\n", end="")
    except Exception as e:
        raise e
