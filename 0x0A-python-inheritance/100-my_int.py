#!/usr/bin/python3
""" my_int module
"""


class MyInt(int):
    """ defines MyInt
    """
    def __init__(self, anInt):
        """ Initializes an integer
        """
        self.anInt = anInt

    def __eq__(self, otherInt):
        """ reverses the behavior of ==
        """
        return self.anInt != otherInt

    def __ne__(self, otherInt):
        """ reverses the behavior of !=
        """
        return self.anInt == otherInt
