#!/usr/bin/python3
"""Task5 Module"""
import json


def load_from_json_file(filename):
    """json file to obj"""
    with open(filename, 'r', encoding="utf-8") as file:
        json.load(file)
