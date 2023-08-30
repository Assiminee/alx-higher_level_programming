#!/usr/bin/python3
import math
""" defines MagicClass """


class MagicClass:
    """ body of MagicClass """
    def __init__(self, radius=0):
        """ initializes an instance of MagicClass class """
        if type(radius) is not int or type(radius) is not float:
            TypeError('radius must be a number')
            self.__radius = None
        else:
            self.__radius = 0

    def area(self):
        """ return area of instance """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ returns circumference of instance """
        return 2 * math.pi * self.__radius
