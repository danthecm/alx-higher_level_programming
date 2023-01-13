#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_score = max(list(a_dictionary.values()))
    student_names = list(a_dictionary.keys())
    return student_names[list(a_dictionary.values()).index(best_score)]
