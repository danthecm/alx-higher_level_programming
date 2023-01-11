#!/usr/bi/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string == None:
        return 0
    result = 0
    for index, i in enumerate(roman_string):
        if i == "M":
            result += 1000        
        elif i == "D":
            result += 500
        elif i == "C":
            result += 100
        elif i == "L":
            result += 50
        elif i == "X":
            result += 10
        elif i == "V":
            if roman_string[index - 1] != "I":
                result += 5
        elif i == "I":
            result += 1
