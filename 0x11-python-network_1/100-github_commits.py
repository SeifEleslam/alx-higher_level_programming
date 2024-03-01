#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests
from sys import argv as args

if __name__ == "__main__":
    """Don't Run on Import"""
    url = f"https://api.github.com/repos/{args[1]}/{args[2]}/commits"
    headers = {"Accept": "application/vnd.github+json",
               "X-GitHub-Api-Version": "2022-11-28"}
    res = requests.get(url, headers=headers)
    commits = res.json()
    for commit in commits:
        author = commit.get('commit').get('author').get('name')
        print(f"{commit.get('sha')}: {author}")
