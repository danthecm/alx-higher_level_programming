#!/usr/bin/python3
"""
A module containing a function that appends to a file
and returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8)
    and returns the number of characters written.

    :param filename: The name of the file to be written.
        If the file does not exist, it will be created.
        If it already exists, its content will be overwritten.
        Default value is an empty string ('').
    :param text: The string to be written to the file.
        Default value is an empty string ('').
    :return: The number of characters written to the file.
    """
    with open(filename, "a", encoding="utf8") as file:
        file.write(text)
    return len(text)
