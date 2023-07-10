#!/usr/bin/python3
"""
a function that checks if the object is an instance of a class
that inherited (directly or indirectly) from the specified class
"""


def inherits_from(obj, a_class):
    """
    Return:
        True if the object is an instance of a class that inherited
        (directly or indirectly) from the specified class
        otherwise False
    """
    return (issubclass(type(obj), a_class) and type(obj) is not a_class)
