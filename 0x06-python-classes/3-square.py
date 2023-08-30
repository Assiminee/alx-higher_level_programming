#!/usr/bin/python3
""" defines a square """


class Square:
    """ Square class body """
    def __init__(self, size=0):
        """ initializes an instance of Square class """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """ computes and returns area of a square """
        return self.__size ** 2
