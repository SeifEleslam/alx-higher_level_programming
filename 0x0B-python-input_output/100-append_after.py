#!/usr/bin/python3
"""Pascal Module"""


def append_after(filename="", search_string="", new_string=""):
    """after each specified line"""
    with open(filename, 'r', encoding="utf-8") as file:
        lines = file.readlines()
    for i in range(len(lines)):
        if search_string in lines[i]:
            lines[i] += new_string
    print(lines)
    with open(filename, 'w', encoding="utf-8") as file:
        file.writelines(lines)
