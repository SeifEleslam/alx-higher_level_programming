#!/usr/bin/python3
"""Requesting Status wit urllib"""
from urllib.request import Request, urlopen
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    with urlopen(Request(args[1])) as res:
        res = res.getheader('X-Request-Id')
        print(res)
