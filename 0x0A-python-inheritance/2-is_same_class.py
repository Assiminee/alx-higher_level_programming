#!/usr/bin/python3
""" is_same_class module
"""


def is_same_class(obj, a_class):
    """ Returns True if obj is exactly
    an instance of a_class, otherwise
    it returns False
    """
    if type(obj) == a_class:
        return True
    return False
