#!/usr/bin/python3
"""Magic Class"""
import math


class MagicClass:
    """Magic Class Structure"""

    def __init__(self, radius):
        """Initialize Magic Class"""
        self.__radius = 0
        if type(radius) is not int:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Area Calc"""
        return self.__radius**2 * math.pi

    def circumference(self):
        """Circumference Calc"""
        return 2 * self.__radius * math.pi
