#!/usr/bin/python3
""" a script that displays the value of X-Request-Id """

import requests
from sys import argv

if __name__ == "__main__":
    page = requests.get(argv[1])
    print(page.headers.get('X-Request-Id'))
