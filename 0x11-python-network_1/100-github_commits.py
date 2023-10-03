#!/usr/bin/python3
"""a script that takes your GitHub credentials and displays your id"""

import requests
from sys import argv

if __name__ == "__main__":
    repo = argv[1]
    user = argv[2]
    url = f"https://api.github.com/repos/{user}/{repo}/commits"
    commits = requests.get(url)
    for index in commits.json()[:10]:
        print(
            f"{index.get('sha')}: \
{index.get('commit').get('author').get('name')}"
        )
