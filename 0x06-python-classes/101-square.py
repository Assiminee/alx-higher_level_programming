#!/usr/bin/python3
""" defines a square """


class Square:
    """ Square class body """
    def __init__(self, size=0, position=(0, 0)):
        """ initializes an instance of Square class """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ a getter for the instance attribute 'position' """
        return self.__position

    @position.setter
    def position(self, value):
        """ a setter for the instance attribute 'position' """
        if not (isinstance(value, tuple)
                and len(value) == 2
                and isinstance(value[0], int)
                and isinstance(value[1], int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise ValueError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def __str__(self):
        modified = ""
        string_rep = "\n" * self.__position[1] + (" " * self.__position[0] + "#" * self.__size + "\n") * self.__size
        for i in range(len(string_rep) - 1):
            modified += string_rep[i]
        return modified

    def area(self):
        """ computes and returns area of a square """
        return self.__size ** 2

    def my_print(self):
        """ prints to stdout a square with the character # """
        if self.__size != 0:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0], end="")
                print("#" * self.__size)
        else:
            print()
