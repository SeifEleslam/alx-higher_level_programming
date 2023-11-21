#!/usr/bin/python3
"""Module of first task that contains class square"""


class Square:
    """Represents a square that has a private instance attribute size."""

    def __init__(self, size=0):
        """Intialize size of square with raising the proper error"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Calculate Square Area"""
        return self.__size ** 2


my_square_1 = Square(3)
print("Area: {}".format(my_square_1.area()))

try:
    print(my_square_1.size)
except Exception as e:
    print(e)

try:
    print(my_square_1.__size)
except Exception as e:
    print(e)

my_square_2 = Square(5)
print("Area: {}".format(my_square_2.area()))
