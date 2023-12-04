#!/usr/bin/python3
"""Module to contain is_kind_of_class function"""


def inherits_from(obj, a_class):
    """Return if the obj is instance of class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
