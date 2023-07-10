#!/usr/bin/python3
"""a Rectangle subclass Square"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represent a square"""

    def __init__(self, size):
        """initialize a new square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
