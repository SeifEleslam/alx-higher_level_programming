#!/usr/bin/python3
"""Module to contain custom int class"""


def add_attribute(obj, name, val):
    """Add attribute to object"""

    if hasattr(obj, name) or hasattr(obj, "__dict__"):
        setattr(obj, name, val)
    else:
        raise TypeError("can't add new attribute")
