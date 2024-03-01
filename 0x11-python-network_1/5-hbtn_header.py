#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    res = requests.get(args[1])
    id = res.headers.get('X-Request-Id')
    print(id)
