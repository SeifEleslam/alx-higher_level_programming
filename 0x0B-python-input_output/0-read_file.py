#!/usr/bin/python3
"""Task1 Module"""


def read_file(filename=""):
    """Read file"""
    with open(filename, encoding="utf-8") as file:
        read_data = file.read()
    print(read_data)
