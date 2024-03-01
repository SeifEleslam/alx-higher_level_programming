#!/usr/bin/python3
"""Requesting Status wit urllib"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    try:
        with urlopen(Request(args[1])) as res:
            print(res.read().decode('utf-8'))
    except HTTPError as e:
        print(f"Error code: {e.code}")
