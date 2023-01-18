#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg_len = len(sys.argv) - 1
    print('{} {}'.format(arg_len,arguments if arg_len != 1 else argument, end="")
    print("{}".format('.' if len(sys.argv) < 2 else ':'))
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
