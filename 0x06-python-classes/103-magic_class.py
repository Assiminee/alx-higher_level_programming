#!/usr/bin/python3
""" defines MagicClass """
import math


class MagicClass:
    """ body of MagicClass """
    def __init__(self, radius=0):
        """ initializes an instance of MagicClass class """
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """ return area of instance """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ returns circumference of instance """
        return 2 * math.pi * self._MagicClass__radius
