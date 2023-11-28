#!/usr/bin/python3
"""Magic String Module"""
CALL_COUNT = 0


def magic_string():
    """Returns a Magic string."""
    global CALL_COUNT
    output = "BestSchool, " * CALL_COUNT + "BestSchool"
    CALL_COUNT += 1
    return output
