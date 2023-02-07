#!/usr/bin/python3
"""
Module containing a function that reads a text file
and prints it to stdout
"""


def read_file(filename=""):
    if filename != "":
        with open(filename, "r", "utf-8") as f:
            for line in f:
                print(line, end="")
