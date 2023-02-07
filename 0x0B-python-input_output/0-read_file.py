#!/usr/bin/python3
"""
Module containing a function that reads a text file
and prints it to stdout
"""


def read_file(filename=""):
    """
    Reads a text file and prints it to stdout

    Args:
    filename (str): The filename
    """
    if filename != "":
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                print(line, end="")
