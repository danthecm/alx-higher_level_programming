#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while True:
        try:
            del_index = list(a_dictionary.values()).index(value)
            del_key = list(a_dictionary.keys())[del_index]
            del a_dictionary[del_key]
        except ValueError as e:
            break
    return a_dictionary
