#!/usr/bin/python3
""" write_file module
"""


def write_file(filename="", text=""):
    """ writes "text" to "filename"
    """
    with open(filename, "w", encoding="utf-8") as f:
        num_chars = f.write(text)
        return num_chars
