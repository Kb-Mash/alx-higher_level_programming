#!/usr/bin/python3
"""a script that sends a request to the URL and displays the body"""

import requests
from sys import argv

if __name__ == "__main__":
    page = requests.get(argv[1])
    if page.status_code >= 400:
        print("Error code: {}".format(page.status_code))
    else:
        print(page.text)
