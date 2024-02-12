#!/usr/bin/python3
def add_attribute(instance, att_name, att_val):
    """ adds an attribute to a class or raises
    a TypeError if that isn't possible
    """
    if hasattr(instance, att_name):
        instance.att_name = att_val
    else:
        raise TypeError("can't add new attribute")
