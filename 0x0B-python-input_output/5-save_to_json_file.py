#!/usr/bin/python3
"""a JSON file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """write an object to a text file using JSON representation"""
    with open(filename, "w") as fp:
        json.dump(my_obj, fp)
