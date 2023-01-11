#!/usr/bin/python3
def common_elements(set_1, set_2):
    common = []
    for item in set_1:
        if item not in set_2:
            common.append(item)
    return common
