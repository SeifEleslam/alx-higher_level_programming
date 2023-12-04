#!/usr/bin/python3
"""Module to contain Base class"""


class BaseGeometry(object):
    "Empty class"

    def area(self):
        """area raising exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validating integers"""
        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
