#!/usr/bin/python3
"""a script that displays the value of the X-Request-Id variable"""

from sys import argv
import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as res:
        req = res.info()
        print(req.get("X-Request-Id"))
