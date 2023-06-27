#!/usr/bin/python3
"""a class Square that defines a square by: (based on 2-square.py)"""


class Square:
    """defines a square"""
    def __init__(self, size=0):
        """Instantiation with optional size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """returns the current square area"""
        return (self.__size ** 2)
