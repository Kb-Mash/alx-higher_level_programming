#!/usr/bin/python3
"""a text file insertion function"""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file"""
    with open(filename, "r") as fp:
        lines = fp.readlines()

    with open(filename, "w") as fp:
        for line in lines:
            fp.write(line)
            if search_string in line:
                fp.write(new_string + "\n")
