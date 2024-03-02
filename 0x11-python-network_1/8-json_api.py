#!/usr/bin/python3
"""
    sends a POST request to http://0.0.0.0:5000/search_user
    with the letter as a parameter.
"""


import requests
import sys

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        param = {'q': ""}
    else:
        param = {'q': sys.argv[1]}

    resp = requests.post(url, data=param)
    try:
        json_resp = resp.json()
        if json_resp:
            print(f"[{json_resp.get('id')}] {json_resp.get('name')}")
        else:
            print('No result')
    except Exception:
        print('Not a valid JSON')
