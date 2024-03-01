#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    headers = {"Accept": "application/vnd.github+json",
               "Authorization": f"Bearer {args[2]}",
               "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get(f'https://api.github.com/users/{args[1]}',
                       headers=headers)
    print(res.json().get('id'))
