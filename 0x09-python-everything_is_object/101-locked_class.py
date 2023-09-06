#!/usr/bin/python3
""" Locked class module
"""


class LockedClass:
    """Body of LockedClass class
    """
    def __setattr__(self, name, val):
        """Limits which attributes
        can be set
        """
        if name == "first_name":
            self.__dict__[name] = val
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
