#!/usr/bin/python3
"""a string-to-JSON function"""
import json


def from_json_string(my_str):
    """returns the JSON representation of a string object"""
    return json.loads(my_str)
