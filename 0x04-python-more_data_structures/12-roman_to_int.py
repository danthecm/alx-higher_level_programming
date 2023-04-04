#!/usr/bi/python3
def roman_to_int(roman_string):
    result = 0
    if type(roman_string) != str:
        return result
    roman_string = roman_string.upper()
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    for index, letter in enumerate(roman_string):
        if index > 0:
            if roman_string[index] != "I" and roman_string[index - 1] == "I":
                result += -2
        result += roman_numerals.get(letter)
    return result
