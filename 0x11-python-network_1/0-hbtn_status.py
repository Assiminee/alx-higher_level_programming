#!/usr/bin/python3
"""
    fetches https://alx-intranet.hbtn.io/status
"""


import urllib.request

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as resp:
        server_resp = resp.read()

    print("Body response:")
    print(f"\t- type: {type(server_resp)}")
    print(f"\t- content: {server_resp}")
    print(f"\t- utf8 content: {server_resp.decode('utf-8')}")
