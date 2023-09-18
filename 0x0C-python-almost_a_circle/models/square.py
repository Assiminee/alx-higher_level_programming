#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a Square instance"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns the string representation of
        a Square instance
        """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Gets the size of a Square instance"""
        return self.width

    @size.setter
    def size(self, value):
        """sets the size of a Square instance"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns instance attributes"""
        if args:
            i = 0
            atts = ["id", "size", "x", "y"]
            for att in atts:
                setattr(self, att, args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation
        of a Square instance
        """
        atts = ["id", "size", "x", "y"]
        return {att: getattr(self, att) for att in atts}
