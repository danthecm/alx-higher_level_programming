#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    numerator = 0
    denominator = 0

    for item in my_list:
        numerator += (item[0] * item[1])
        denominator += item[1]

    return numerator / denominator
