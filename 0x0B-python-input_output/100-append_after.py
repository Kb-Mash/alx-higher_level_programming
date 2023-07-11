#!/usr/bin/python3
"""a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file"""
    with open(filename) as fp:
        for line in fp:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as fp:
        fp.write(text)
