#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""


import urllib.request
from urllib.parse import urlencode
from urllib.error import HTTPError
from sys import argv


if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            the_page = response.read()
            print(the_page.decode("utf-8"))
    except HTTPError as error:
        print("Error code: {}".format(error.status))
