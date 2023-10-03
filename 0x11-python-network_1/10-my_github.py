#!/usr/bin/python3
"""a script that takes your GitHub credentials and displays your id"""

import requests
from sys import argv

if __name__ == "__main__":
    req = r = requests.get(
        f"https://api.github.com/users/{argv[1]}",
        headers={"Authorization": f"token {argv[2]}"},
    )
    print(req.json().get("id"))
