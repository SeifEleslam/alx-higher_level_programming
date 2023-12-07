#!/usr/bin/python3
"""Base Class"""


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object with a unique id."""
        if id:
            self.id = id
            return
        self.__class__.__nb_objects += 1
        self.id = self.__class__.__nb_objects
