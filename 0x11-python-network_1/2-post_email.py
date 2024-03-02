#!/usr/bin/python3
"""
    Input: URL and an email
    sends a POST request to the passed URL
    with the email as a parameter, and displays
    the body of the response (decoded in utf-8)
"""


import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    email = {'email': sys.argv[2]}
    url = sys.argv[1]

    data = urllib.parse.urlencode(email)
    data = data.encode('utf-8')

    request = urllib.request.Request(url, data, method='POST')
    with urllib.request.urlopen(request) as resp:
        response = resp.read()
        resp_body = response.decode('utf-8')

    print(resp_body)
