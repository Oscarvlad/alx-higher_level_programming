#!/usr/bin/python3
""" takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""


import requests
from sys import argv


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(argv[2], argv[1])
    count = 0
    login = requests.get(url)
    req = login.json()
    for r in req:
        commit = r["commit"]["author"]
        print("{}: {}".format(r["sha"], commit["name"]))
        count += 1
        if count == 10:
            break
