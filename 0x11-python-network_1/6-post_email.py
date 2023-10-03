#!/usr/bin/python3
"""a script that sends a POST request and displays the body"""

import requests
from sys import argv

if __name__ == "__main__":
    text = requests.post(argv[1], data={"email": argv[2]}).text
    print(text)
