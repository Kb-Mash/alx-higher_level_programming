#!/usr/bin/python3

class Square:
    """defines a square by: (based on 2-square.py)"""
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