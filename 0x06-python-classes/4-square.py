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


my_square = Square(89)
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

my_square.size = 3
print("Area: {} for size: {}".format(my_square.area(), my_square.size))

try:
    my_square.size = "5 feet"
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))
except Exception as e:
    print(e)
