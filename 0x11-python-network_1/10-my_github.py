#!/usr/bin/python3
"""
    takes your GitHub credentials (username and password)
    and uses the GitHub API to display your id
"""


import requests
import sys

if __name__ == '__main__':
    url = "http://api.github.com/user"

    resp = requests.get(url, auth=(sys.argv[1], sys.argv[2]))
    print(resp.json().get('id'))
