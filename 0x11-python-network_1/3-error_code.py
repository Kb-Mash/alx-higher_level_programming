#!/usr/bin/python3
"""a script that handles exceptions"""

import urllib.request
from sys import argv

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as err:
        print(f"Error code: {err.code}")
