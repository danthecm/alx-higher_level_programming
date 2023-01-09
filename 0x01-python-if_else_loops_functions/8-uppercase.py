#!/usr/bin/python3
def uppercase(str):
    for char in str:
        print(
            "{}".format(
                char if ord(char) < 97 else chr(ord(char) - 32)
            ),
            end="")
    print("\n", end="")
