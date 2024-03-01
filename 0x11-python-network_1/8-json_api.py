#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args
# http://0.0.0.0:5000/search_user
if __name__ == "__main__":
    """Don't Run on Import"""
    query = args[1] if len(args) == 2 else ''
    res = requests.post('http://0.0.0.0:5000/search_user',
                        data={"q": query})
    try:
        data: dict = res.json()
        if data:
            print(f'[{data.get("id")}] {data.get("name")}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
