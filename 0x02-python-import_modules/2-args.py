#!/usr/bin/python3
if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys
    ac = len(sys.argv) - 1
    if ac == 0:
        print("{} arguments.".format(ac))
    elif ac == 1:
        print("{} argument:".format(ac))
    else:
        print("{} arguments:".format(ac))
    for i in range(ac):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
