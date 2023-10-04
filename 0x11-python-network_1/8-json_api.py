#!/usr/bin/python3
'''script that takes in a letter and sends a POST request to \
http://0.0.0.0:5000/search_user with the letter as a parameter.'''
import requests
from sys import argv


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    q = argv[1] if len(argv) > 1 else ""
    data = {'q': q}
    response = requests.post(url, data)
    if response.headers.get('content-type') != 'application/json':
        print("Not a valid JSON")
    elif response.json() == {}:
        print("No result")
    else:
        print("[{}] {}".format(response.json().get('id'),
                               response.json().get('name')))
