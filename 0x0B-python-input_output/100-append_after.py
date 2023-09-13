#!/usr/bin/python3
""" append_after module
"""


def append_after(filename="", search_string="", new_string=""):
    """ adds "new_string" after each occurence of "seach_string"
    in a file
    """
    new_data = []
    if filename and search_string and new_string:
        with open(filename, encoding="utf-8") as f:
            for line in f:
                new_data.append(line)
                if search_string in line:
                    new_data.append(f"{new_string}")
        with open(filename, "w", encoding="utf-8") as f:
            for data in new_data:
                f.write(data)
