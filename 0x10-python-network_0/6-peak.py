#!/usr/bin/python3
"""Defines a peak-finding algorithm"""


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""
    prev = 0
    for i, num in enumerate(list_of_integers):
        if i:
            prev = list_of_integers[i - 1]
        if i < len(list_of_integers) - 1:
            next = list_of_integers[i + 1]
        else:
            next = 0
        if num >= prev and num >= next:
            return num
