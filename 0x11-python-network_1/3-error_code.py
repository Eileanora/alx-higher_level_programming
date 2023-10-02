#!/usr/bin/python3
'''script that takes ina URL, sends a request \
and displays the body of the response.
manage exceptions and print the error code'''
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
