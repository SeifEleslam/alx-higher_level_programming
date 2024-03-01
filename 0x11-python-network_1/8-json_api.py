#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args
# http://0.0.0.0:5000/search_user
if __name__ == "__main__":
    """Don't Run on Import"""
    query = args[1] if len(args) > 1 else ''
    res = requests.post('http://0.0.0.0:5000/search_user',
                        params={"q": query})
    try:
        data: dict = res.json()
        print(data)
        if data:
            print(f'[{data.get("id")}] {data.get("name")}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")