#!/usr/bin/python3
"""
a function that checks if the object is an instance of,
or if the object is an instance of a class that inherited from,
the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Return:
        True if the object is an instance of,
        or if the object is an instance of a class that inherited from,
        the specified class ; else False
    """
    return (isinstance(obj, a_class))
