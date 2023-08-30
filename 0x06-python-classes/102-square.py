#!/usr/bin/python3
""" defines a square """


class Square:
    """ Square class body """
    def __init__(self, size=0):
        """ initializes an instance of Square class """
        self.size = size

    @property
    def size(self):
        """ a getter for the instance attribute 'size' """
        return self.__size

    @size.setter
    def size(self, value):
        """ a setter for the instance attribute 'size' """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ computes and returns area of a square """
        return self.__size ** 2

    def __eq__(self, sqr):
        """ checks if two objects have equal area values """
        return self.area() == sqr.area()

    def __ne__(self, sqr):
        """ checks if two objects have different area values """
        return self.area() != sqr.area()

    def __gt__(self, sqr):
        """ checks if calling object has higher area value """
        return self.area() > sqr.area()

    def __ge__(self, sqr):
        """ checks if calling object's area value
        is higher than or equal to sqr's """
        return self.area() >= sqr.area()

    def __lt__(self, sqr):
        """ checks if calling object has lower area value """
        return self.area() < sqr.area()

    def __le__(self, sqr):
        """ checks if calling object's area value
        is less than or equal to sqr's """
        return self.area() <= sqr.area()
