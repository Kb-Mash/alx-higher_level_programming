#!/usr/bin/python3
"""a function that appends text to a file"""


def append_write(filename="", text=""):
    """returns the number of characters appended"""
    with open(filename, "a", encoding="utf-8") as fp:
        fp.write(text)
        return len(text)
