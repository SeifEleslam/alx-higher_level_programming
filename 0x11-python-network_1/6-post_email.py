#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    res = requests.post(args[1], {"email": args[2]})
    print(res.content.decode('utf-8'))
