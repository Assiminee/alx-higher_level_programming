#!/usr/bin/python3
""" Rectangle Module
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Defines a square
    """
    def __init__(self, size):
        """ Initializes a square
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """ Returns the area of a square
        """
        return self.__size ** 2
