#!/usr/bin/python3
"""a function that writes to a file"""


def write_file(filename="", text=""):
    """returns the number of characters written"""
    with open(filename, "w", encoding="utf-8") as fp:
        fp.write(text)
        return len(text)
