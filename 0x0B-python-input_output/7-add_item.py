#!/usr/bin/python3
"""
A script that creates a list from command line arguments
and saves it to a json file
"""

import sys


save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file
args_list = sys.argv[1:]


with open("add_item.json", "a+") as file:
    loaded_file = []
    if file.seek(0, 1) != 0:
        loaded_file = load_from_json_file("add_item.json")
    for item in args_list:
        loaded_file.append(item)
    save_to_json_file(loaded_file, "add_item.json")
