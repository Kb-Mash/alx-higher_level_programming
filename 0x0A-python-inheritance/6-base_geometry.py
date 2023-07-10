#!/usr/bin/python3
"""a class BaseGeometry"""


class BaseGeometry:
    """represent base geometry"""

    def area(self):
        """when not implemented"""
        raise Exception("area() is not implemented")
