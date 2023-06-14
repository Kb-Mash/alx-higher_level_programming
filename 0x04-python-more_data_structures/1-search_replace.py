#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element by another in a new list"""
    return (list(map(lambda i: replace if i is search else i, my_list)))
