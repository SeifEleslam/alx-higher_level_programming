#!/usr/bin/python3
"""Task2 Module"""


def append_write(filename="", text=""):
    """Write to file"""
    with open(filename, 'a', encoding="utf-8") as file:
        written_data = file.write(text)
    return (written_data)
