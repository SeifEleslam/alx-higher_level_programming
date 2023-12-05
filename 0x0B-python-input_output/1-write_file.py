#!/usr/bin/python3
"""Task2 Module"""


def write_file(filename="", text=""):
    """Write to file"""
    with open(filename, 'w', encoding="utf-8") as file:
        written_data = file.write(text)
    return (written_data)
