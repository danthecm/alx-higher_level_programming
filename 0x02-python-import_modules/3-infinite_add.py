#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args_list = sys.argv[1:]
    result = sum([int(num) for num in args_list])
    print("{}".format(result))
