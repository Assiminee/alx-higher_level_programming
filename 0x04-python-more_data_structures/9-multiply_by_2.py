#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for item in a_dictionary.items():
        key, value = item
        new_dict[key] = value * 2
    return new_dict
