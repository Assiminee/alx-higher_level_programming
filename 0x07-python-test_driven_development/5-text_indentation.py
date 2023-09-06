#!/usr/bin/python3
"""
text_indentation module
"""


def text_indentation(text):
    """
    prints "text" with 2 new lines after each of these
    characters: "." "?" and ":"
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    while i < len(text):
        if text[i] in [".", "?", ":"]:
            print("{}\n".format(text[i]))
            i += 1
            while len(text) > i:
                if text[i] == " ":
                    i += 1
                else:
                    break
        else:
            print("{}".format(text[i]), end="")
            i += 1
