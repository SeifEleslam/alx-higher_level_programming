#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    query = args[2] if len(args) > 2 else ''
    res = requests.post(args[1], params={"q": query})
    try:
        data = res.json()
        if data:
            print(f'[{data['id']}] {data['name']}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
    
