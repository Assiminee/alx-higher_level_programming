#!/usr/bin/python3
""" append_write module
"""


def append_write(filename="", text=""):
    """ appends "text" to the end of
    "filename"
    """
    with open(filename, "a", encoding="utf-8") as f:
        num_chars = f.write(f"{text}")
        return num_chars
