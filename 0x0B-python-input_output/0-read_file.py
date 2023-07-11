#!/usr/bin/python3
"""a text file-reading function"""


def read_file(filename=""):
    """prints the contents of a UTF8 text file to stdout"""
    with open(filename, "r", encoding="utf-8") as fp:
        print(fp.read(), end="")
