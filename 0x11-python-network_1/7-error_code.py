#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    res = requests.get(args[1])
    print(res.content.decode() if res.ok
          else f"Error code: {res.status_code}")
