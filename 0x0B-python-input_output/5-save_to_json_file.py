#!/usr/bin/python3
"""Task5 Module"""
import json


def save_to_json_file(my_obj, filename):
    """str to obj"""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
