#!/usr/bin/python3
"""Module of first task that contains class square"""


class Square:
    """Represents a square that has a private instance attribute size."""

    def __init__(self, size=0):
        """Intialize size of square with raising the proper error"""
        self.size = size

    def area(self):
        """Calculate Square Area"""
        return self.__size ** 2

    @property
    def size(self):
        """Get the value of Size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Get the value of Size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def __lt__(self, other):
        """Compare Two Squares"""
        return self.area() < other.area()

    def __gt__(self, other):
        """Compare Two Squares"""
        return self.area() > other.area()

    def __le__(self, other):
        """Compare Two Squares"""
        return self.area() <= other.area()

    def __ge__(self, other):
        """Compare Two Squares"""
        return self.area() >= other.area()

    def __eq__(self, other):
        """Compare Two Squares"""
        return self.area() == other.area()

    def __ne__(self, other):
        """Compare Two Squares"""
        return self.area() != other.area()
