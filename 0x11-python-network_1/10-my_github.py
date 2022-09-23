#!/usr/bin/python3
""" takes in a letter and sends a POST request
    to http://0.0.0.0:5000/search_user with the
    letter as a parameter.
"""


import requests
from sys import argv


if __name__ == "__main__":
    username = argv[1]
    headers = {'Authorization': 'token ' + argv[2]}
    login = requests.get('https://api.github.com/user', headers=headers)
    req = login.json()
    if 'id' in req:
        print(req['id'])
    else:
        print(None)
