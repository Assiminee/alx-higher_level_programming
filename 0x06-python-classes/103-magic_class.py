#!/usr/bin/python3
""" defines MagicClass """
import math


class MagicClass:
    """ body of MagicClass """
    def __init__(self, radius=0):
        """ initializes an instance of MagicClass class """
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            TypeError('radius must be a number')
        self._MagicClass__radius = float(radius)

    def area(self):
        """ return area of instance """
        return (self._MagicClass__radius ** 2) * math.pi

    def circumference(self):
        """ returns circumference of instance """
        return 2 * math.pi * self._MagicClass__radius
