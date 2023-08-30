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

    def my_print(self):
        """ prints to stdout a square with the character # """
        if self.__size != 0:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
        else:
            print()
