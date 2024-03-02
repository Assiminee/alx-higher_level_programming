#!/usr/bin/python3
"""
    Time for an interview!
"""


if __name__ == "__main__":
    from requests import get
    from sys import argv

    url = f"https://api.github.com/repos/{argv[2]}/{argv[1]}/commits"
    commits = get(url).json()
    try:
        for i in range(10):
            sha_comms = commits[i].get("sha")
            author_name = commits[i].get("commit").get("author").get("name")
            print(f"{sha_comms}: {author_name}")
    except Exception:
        pass
