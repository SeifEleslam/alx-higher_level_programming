#!/usr/bin/python3
"""Module of first task that contains class square"""


class Square:
    """Represents a square that has a private instance attribute size."""
    __size = 0

    def __init__(self, size):
        Square.__size = size
