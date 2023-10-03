#!/usr/bin/python3
"""a script that sends POST request and displays body of the response"""

from urllib.parse import urlencode
from urllib.request import Request, urlopen
from sys import argv

if __name__ == "__main__":
    value = {"email": argv[2]}
    data = urlencode(value).encode("ascii")
    req = Request(argv[1], data)

    with urlopen(req) as res:
        print(res.read().decode("utf-8", "replace"))
