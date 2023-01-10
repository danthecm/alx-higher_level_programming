#!/usr/bin/python3
def no_c(my_string=""):
    new_string = ""
    for string in my_string:
        if string != 'C' and string != 'c':
            new_string += string
    return new_string
