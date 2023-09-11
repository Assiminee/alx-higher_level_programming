#!/usr/bin/python3
""" MyList module
"""


class MyList(list):
    """ Defines MyList class
    """
    def print_sorted(self):
        """ Prints a list sorted
        in ascending order
        """
        print(sorted(self))
