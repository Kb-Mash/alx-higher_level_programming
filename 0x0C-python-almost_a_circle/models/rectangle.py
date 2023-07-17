#!/usr/bin/python3
"""a class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """defines a Rectangle instance"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Instantiation of a Rectangle instance

        Args:
            width: width of object
            height: height of object
            x (optional): x-coordinate of object
            y (optional): y-coordinate of object
            id (int, optional): id of object
        """
        super().__init__(id)
        self.validate(width, "width")
        self.validate(height, "height")
        self.validate(x, "x")
        self.validate(y, "y")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def validate(self, value, name):
        """validation for all setter methods and instantiation"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (name == "width" or name == "height") and value <= 0:
            raise ValueError("{} must be > 0".format(name))
        if (name == "y" or name == "x") and value < 0:
            raise ValueError("{} must be >= 0".format(name))

    @property
    def width(self):
        """retrieves the width of object"""
        return self.__width

    @width.setter
    def width(self, width):
        """sets the width of object"""
        self.validate(width, "width")
        self.__width = width

    @property
    def height(self):
        """retrieves the height of object"""
        return self.__height

    @height.setter
    def height(self, height):
        """sets the height of the object"""
        self.validate(height, "height")
        self.__height = height

    @property
    def x(self):
        """retrieves the x coordinate of the object"""
        return self.__x

    @x.setter
    def x(self, x):
        """sets the x coordinate of the object"""
        self.validate(x, "x")
        self.__x = x

    @property
    def y(self):
        """retrievss the y coordinate of the object"""
        return self.__y

    @y.setter
    def y(self, y):
        """sets the y coordinate of the object"""
        self.validate(y, "y")
        self.__y = y

    def area(self):
        """returns area of Rectangle instance"""
        return self.height * self.width

    def display(self):
        """
        prints the instance using # character

        y - vertical offset
        x - horizontal offset
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """return string representation of the rectangle object"""
        string = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.x, self.y, self.width, self.height)
        return string

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute"""
        if args:
            attr = ["id", "width", "height", "x", "y"]
            i = 0
            for arg in args:
                setattr(self, attrs[i], arg)
                i += 1
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representation of the Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
