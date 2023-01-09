#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    try:
        a = 1
        b = 2
        print("{:d} + {:d} = {:d}".format(a, b, add(1, 2)))
    except Exception as e:
        raise e
