#!/usr/bin/python3
"""a class Square that inherits from Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a Square instance"""
    def __init__(self, size, x=0, y=0, id=None):
        """
        instantiation of Square instance

        Args:
            size: size of square
            x: x-coordinate
            y: y-coordinate
            id: id of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """retrieves the size of the square object"""
        return self.width

    @size.setter
    def size(self, value):
        self.validate(value, "width")
        self.width = value
        self.height = value

    def __str__(self):
        """returns a string representation of the Square object"""
        string = "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)
        return string

    def update(self, *args, **kwargs):
        """Updates attributes with provided arguments and keyword arguments"""
        if args:
            attrs = ["id", "size", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
