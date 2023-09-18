#!/usr/bin/python3
""" Rectangle module
"""
from .base import Base


class Rectangle(Base):
    """ Defines a Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for the private insatance
        variable width
        """
        return self.__width

    @width.setter
    def width(self, width):
        """ setter for the private insatance
        variable width
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ getter for the private insatance
        variable height
        """
        return self.__height

    @height.setter
    def height(self, height):
        """ setter for the private insatance
        variable height
        """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """ getter for the private insatance
        variable x
        """
        return self.__x

    @x.setter
    def x(self, x):
        """ setter for the private insatance
        variable x
        """
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """ getter for the private insatance
        variable y
        """
        return self.__y

    @y.setter
    def y(self, y):
        """ setter for the private insatance
        variable y
        """
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Computes and returns the area
        of a Rectangle instance
        """
        return self.__height * self.__width

    def display(self):
        """ prints in stdout the Rectangle
        instance with the character #
        """
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        print((("\n" * y) + (" " * x + "#" * width + "\n") * height)[:-1])

    def __str__(self):
        """ Returns the string representation
        of a Rectangle instance
        """
        id = self.id
        width = self.__width
        height = self.__height
        x = self.__x
        y = self.__y
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute
        """
        if args:
            i = 0
            atts = ["id", "width", "height", "x", "y"]
            for att in atts:
                if i == len(args):
                    break
                setattr(self, att, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Returns the dictionary definition of
        a Rectangle instance
        """
        atts = ["id", "width", "height", "x", "y"]
        return {att: getattr(self, att) for att in atts}
