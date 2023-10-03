#!/usr/bin/python3
"""a script that sends a POST request with the letter as a parameter"""

import requests
from sys import argv

if __name__ == "__main__":
    q = "" if len(argv) == 1 else argv[1]
    req = requests.post("http://0.0.0.0:5000/search_user", {"q": q})

    try:
        response = req.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
