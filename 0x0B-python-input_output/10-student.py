#!/usr/bin/python3
"""Task9 Module"""


class Student():
    """Student class for task 9."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        output = {}
        for attr in attrs:
            if hasattr(self, attr):
                output[attr] = getattr(self, attr)
        return output
