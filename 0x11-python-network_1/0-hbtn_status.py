#!/usr/bin/python3
"""Requesting Status wit urllib"""
from urllib.request import Request, urlopen
if __name__ == "__main__":
    """Don't Run on Import"""
    with urlopen(Request(
            'https://alx-intranet.hbtn.io/status')) as res:
        res = res.read()
        print("Body response:")
        print(f"    - type: {type(res)}")
        print(f"    - content: {res}")
        print(f"    - utf8 content: {res.decode('utf-8')}")
