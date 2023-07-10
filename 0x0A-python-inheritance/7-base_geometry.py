#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """represents base geometry"""
    def area(self):
        """when not yet implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
