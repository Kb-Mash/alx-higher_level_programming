#!/usr/bin/python3
"""a function that prints a square with the character #"""


def print_square(size):
    """Raises:
        TypeError: If size is not an integer.
        ValueError: If size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
