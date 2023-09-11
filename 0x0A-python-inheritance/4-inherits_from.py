#!/usr/bin/python3
""" inherits_from module
"""


def inherits_from(obj, a_class):
    """ Returns True if obj is an instance of a class
    that inherited (directly or indirectly) a_class
    otherwise it returns False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
