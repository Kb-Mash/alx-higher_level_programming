#!/bin/python3

if __name__ == "__main__":
    """handles basic operations"""
    from calculator_1 import add, sub, mul, div
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    ops = {'+': add, '-': sub, '*': mul, '/': div}
    a = int(sys.argv[1])
    op = sys.argv[2]
    b = int(sys.argv[3])
    if op in ops:
        result = ops[op](a, b)
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, result))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
