#!/usr/bin/python3
"""Module of first task that contains class square"""


class Square:
    """Represents a square that has a private instance attribute size."""

    def __init__(self, size=0, position=(0, 0)):
        """Intialize size of square with raising the proper error"""
        self.size = size
        self.position = position

    def area(self):
        """Calculate Square Area"""
        return self.size ** 2

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

    @property
    def position(self):
        """Get the value of Size"""
        return self.__position

    @position.setter
    def position(self, value):
        """Get the value of Size"""
        if len(value) != 2 or not self.is_tuple_valid(value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def is_tuple_valid(self, tup):
        for ele in tup:
            if (not isinstance(ele, int)) or ele < 0:
                return False
        return True

    def my_print(self):
        """Print the Square with char #"""
        if self.size == 0:
            print()
            return
        print("\n" * self.position[1], end="")
        for i in range(self.size):
            print("{}{}".format(" " * (self.position[0]), "#" * (self.size)))


my_square_1 = Square(3)
my_square_1.my_print()

print("--")

my_square_2 = Square(3, (1, 1))
my_square_2.my_print()

print("--")

my_square_3 = Square(3, (3, 0))
my_square_3.my_print()

print("--")
