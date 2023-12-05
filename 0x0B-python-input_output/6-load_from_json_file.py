#!/usr/bin/python3
"""Task5 Module"""
import json


def load_from_json_file(filename):
    """json file to obj"""
    with open(filename, 'r') as file:
        return json.load(file)
