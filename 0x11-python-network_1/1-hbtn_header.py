#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
    found in the header of the response.
"""


import urllib.request
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as response:
        for head in response.headers.items():
            if head[0] == 'X-Request-Id':
                print(head[1])
