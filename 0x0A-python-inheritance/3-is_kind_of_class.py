#!/usr/bin/python3
""" is_kind_of_class module
"""


def is_kind_of_class(obj, a_class):
    """ Returns True if obj is an instance of a_class
    or is an instance of a class that inherited from a_class,
    otherwise it returns False
    """
    if isinstance(obj, a_class):
        return True
    return False
