#!/usr/bin/python3
"""Module to contain Base class"""


class BaseGeometry(object):
    "Empty class"

    def area(self):
        raise Exception("area() is not implemented")
