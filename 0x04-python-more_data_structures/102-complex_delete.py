#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        keys = []
        for tp in a_dictionary.items():
            key, val = tp
            if val == value:
                keys.append(key)
        for key in keys:
            del a_dictionary[key]
        return a_dictionary
