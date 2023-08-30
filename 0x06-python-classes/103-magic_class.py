#!/usr/bin/python3
""" defines MagicClass """
import math


class MagicClass:
    """ body of MagicClass """
    def __init__(self, radius):
        """ initializes an instance of MagicClass class """
        self.__radius = 0
        if type(radius) is str and radius.isdigit():
            radius = int(radius)
        if type(radius) is not int and type(radius) is not float:
            TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """ return area of instance """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """ returns circumference of instance """
        return 2 * math.pi * self._MagicClass__radius
