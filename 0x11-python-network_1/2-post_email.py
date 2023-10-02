#!/usr/bin/python3
'''script that takes a URL and an email and sends a \
POST request to the passed URL with the email as a parameter, \
and displays the body of the response (decoded in utf-8)'''
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    # convert email to key-value pair
    # to be able to send it in the body of the post request
    data = urllib.parse.urlencode({'email': email})
    # convert data to bytes
    data = data.encode('ascii')

    with urllib.request.urlopen(url, data) as reponse:
        print(reponse.read().decode('utf-8'))
