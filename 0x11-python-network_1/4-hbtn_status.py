#!/usr/bin/python3
"""Requesting Status wit urllib"""
import requests

if __name__ == "__main__":
    """Don't Run on Import"""
    res = requests.get('https://alx-intranet.hbtn.io/status')
    content = res.content.decode("utf-8")
    print("Body response:")
    print(f"\t- type: {type(content)}")
    print(f"\t- content: {content}")
