#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file"""
import json
import sys


if __name__ == "__main__":
    def save_to_json_file(my_obj, filename):
        """write an object to a text file using JSON representation"""
        with open(filename, "w") as fp:
            json.dump(my_obj, fp)

    def load_from_json_file(filename):
        """create a Python object from a JSON file"""
        with open(filename, "r") as fp:
            return json.load(fp)

    try:
        items = load_from_json_file("add_item.json")
    except FileNotFoundError:
        items = []

    items.extend(sys.argv[1:])
    save_to_json_file(items, "add_item.json")
