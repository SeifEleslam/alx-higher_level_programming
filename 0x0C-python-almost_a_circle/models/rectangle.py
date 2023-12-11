#!/usr/bin/python3
"""Rectangle Class Module"""
from base import Base


class Rectangle(Base):
    """A class to represent a rectangle. Inherits from the 'base' class."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize size of square with raising the proper error"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """String representation for rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(
            type(self).__name__, self.id, self.x, self.y,
            self.width, self.height)

    @property
    def width(self):
        """Get the value of rectangle width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set the value of rectangle width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get the value of rectangle height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set the value of rectangle height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get the value of rectangle x"""
        return self.__x

    @x.setter
    def x(self, value):
        """set the value of rectangle x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get the value of rectangle y"""
        return self.__y

    @y.setter
    def y(self, value):
        """set the value of rectangle y"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """Update the position and size of the rectangle."""
        attrs = ["width", "height", "x", "y"]
        if len(args) > 0:
            super().__setattr__("id", args[0])
            for i in range(1, len(args)):
                if i-1 in range(len(attrs)):
                    setattr(self, attrs[i-1], args[i])
        for key in kwargs:
            if key == "id":
                super().__setattr__("id", kwargs[key])
            elif key in attrs:
                setattr(self, key, kwargs[key])

    def area(self):
        """Calculate rectangle Area"""
        return self.width * self.height

    def display(self):
        """Display Rectangle using # char"""
        for i in range(self.y):
            print()
        for i in range(self.height):
            print("{}".format(" " * self.x + "#" * self.width))

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        newDic = {}
        for key, val in vars(self).items():
            newDic[key.replace("_", "").replace("Rectangle", "")] = val
        return newDic
