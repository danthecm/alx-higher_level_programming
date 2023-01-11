#!/usr/bin/python3
def remove_char_at(my_string, n):
    if n < 0:
        return my_string
    return my_string[:n] + "" + my_string[n + 1:]
