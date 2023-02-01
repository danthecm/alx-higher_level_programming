#!/usr/bin/python3
"""
A module containing a text_indentation function
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :
    """
    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = ""
    specials = [".", "?", ":"]
    for index, character in enumerate(text):
        if character in specials:
            new_text += f"{character}\n\n"
            continue
        if character == " " and len(text) > index + 1:
            if text[index - 1] in specials or text[index + 1] in specials:
                continue
            elif text[index - 1] == " " and text[index + 1] == " ":
                continue
        new_text += character
    print(new_text)
