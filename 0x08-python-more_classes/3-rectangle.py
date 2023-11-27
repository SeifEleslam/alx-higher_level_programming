
#!/usr/bin/python3
"""Module of first task that contains class square"""


class Rectangle:
    """Represents a REc that has a private instance attribute size."""

    def __init__(self, width=0, height=0):
        """Intialize size of square with raising the proper error"""
        self.height = height
        self.width = width

    def area(self):
        """Calculate Rec Area"""
        return self.height * self.width

    def perimeter(self):
        """Calculate Rec Perimeter"""
        return (self.height + self.width)*2 if (
            self.height > 0 and self.width > 0) else 0

    @property
    def width(self):
        """Get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def is_tuple_valid(self, tup):
        for ele in tup:
            if (not isinstance(ele, int)) or ele < 0:
                return False
        return True

    def __str__(self):
        """String represintaion for Rec"""
        output = ""
        for i in range(self.height):
            output += "{}\n".format("#" * (self.width))
        return "" if (self.width == 0 or self.width == 0
                      )else output[0:-1]
