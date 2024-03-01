#!/usr/bin/python3
"""Requesting Status wit urllib"""
from urllib.request import Request, urlopen
from urllib.parse import urlencode
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    data = urlencode({"email": args[2]}).encode('utf-8')
    with urlopen(Request(args[1], data, method='POST')) as res:
        print(res.read().decode('utf-8'))
