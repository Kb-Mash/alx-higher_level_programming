#!/usr/bin/python3

def magic_calculation(a, b):
    """functions the same as the bytecode provided"""
    from magic_calculation_102 import add, sub

    if a < b:
        c = add(a, b)
        for index in range(4, 6):
            c = add(c, index)
        return (c)

    else:
        return (sub(a, b))
