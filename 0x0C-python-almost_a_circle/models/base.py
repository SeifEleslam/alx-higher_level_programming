#!/usr/bin/python3
"""Base Class"""
import json


class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the object with a unique id."""
        if id:
            self.id = id
            return
        self.__class__.__nb_objects += 1
        self.id = self.__class__.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Convert a list of dictionaries to a JSON string."""
        list_dictionaries = [] if list_dictionaries is None else list_dictionaries
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """to json"""
        json_list = json.loads(json_string)
        return [] if json_list is None else json_list

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the list of objects to a file."""
        list_objs = [] if list_objs is None else list_objs
        json_string = cls.to_json_string(
            list(map(lambda x: x.to_dictionary(), list_objs)))
        with open(f"{cls.__name__}.json", "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Create an object from a dictionary."""
        shape = cls(1) if cls.__name__ == "Square"else cls(1, 1)
        cls.update(shape, **dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """Load the list of objects from a file."""
        try:
            with open(f"{cls.__name__}.json", "r") as file:
                return list(map(lambda x: cls.create(**x), cls.from_json_string(file.read())))
        except Exception as e:
            return []
