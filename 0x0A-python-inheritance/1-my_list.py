#!/usr/bin/python3
"""a class MyList that inherits from list"""


class MyList(list):
    """a function that prints the list, but sorted"""
    def print_sorted(self):
        """prints list"""
        print(sorted(self))
