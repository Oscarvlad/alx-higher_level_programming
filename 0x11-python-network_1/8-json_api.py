#!/usr/bin/python3
""" takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""


import requests
from sys import argv


if __name__ == "__main__":
    if len(argv) >= 2:
        data = {'q': argv[1]}
    else:
        data = {'q': ""}
    req = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        retrieved = req.json()
        if len(retrieved) > 0:
            print("[{}] {}".format(retrieved['id'], retrieved['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
