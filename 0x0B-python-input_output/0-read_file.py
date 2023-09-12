#!/usr/bin/python3
"""read_file module
"""


def read_file(filename=""):
    """ reads the contents of a file
    """
    with open(filename, encoding="utf-8") as f:
        print(f"{f.read()}", end="")
