#!/usr/bin/python3
"""a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """creates a Python object from a JSON file"""
    with open(filename, "r") as fp:
        return json.load(fp)
