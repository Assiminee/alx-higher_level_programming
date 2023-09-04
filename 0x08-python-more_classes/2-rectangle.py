#!/usr/bin/python3
"""Rectangle Module
"""


class Rectangle:
    """Defines a rectangle
    """
    def __init__(self, width=0, height=0):
        """Initializes an instance of the
        Rectangle class
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Returns the private instance
        variable "width"
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for the private instance
        variable "width"
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the private instance
        variable "height"
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for the private instance
        variable "height"
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle
        """
        if not self.__width or not self.__height:
            return 0
        return 2 * (self.__width + self.__height)
