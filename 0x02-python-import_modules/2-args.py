#!/usr/bin/python3
import sys

if __name__  == '__main__':
    print(
            '{} arguments'.format(len(sys.argv) - 1),
            end=f"{'.' if len(sys.argv) < 2 else ':'}\n"
        )
    for i in range(1, len(sys.argv)):
        print("{}: {}".format(i, sys.argv[i]))
