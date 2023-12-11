#!/usr/bin/python3
"""Base Class"""
import json
import csv
import turtle
import random
from contextlib import closing


class Base:
    """A class to represent the base of a game."""
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
        return "[]" if type(list_dictionaries) != list else (
            json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """to json"""
        return [] if type(json_string) != str else (
            json.loads(json_string))

    @classmethod
    def get_heads(cls):
        """Return all heads in the class."""
        return ["id", "width", "height", "x", "y"
                ] if cls.__name__ == "Rectangle" else [
            "id", "size", "x", "y"]

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
        shape = cls(1) if cls.__name__ == "Square" else cls(1, 1)
        shape.update(**dictionary)
        return shape

    @classmethod
    def load_from_file(cls):
        """Load the list of objects from a file."""
        try:
            with closing(open(f"{cls.__name__}.json", "r")) as file:
                return list(map(lambda x: cls.create(
                    **x), cls.from_json_string(file.read())))
        except (FileNotFoundError):
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the list of objects to a CSV file."""
        list_objs = [] if not list_objs else list_objs
        heads = cls.get_heads()
        with open(f"{cls.__name__}.csv", "w") as file:
            writer = csv.writer(file)
            writer.writerow(heads)
            for row in list_objs:
                dic = row.to_dictionary()
                writer.writerow(list(map(lambda x: dic[x], heads)))

    @classmethod
    def load_from_file_csv(cls):
        """Load the list of objects from a CSV file."""
        output = []
        heads = cls.get_heads()
        try:
            with closing(open(f"{cls.__name__}.csv", "r")) as file:
                reader = csv.DictReader(file)
                for row in reader:
                    for key in row:
                        row[key] = int(row[key])
                    output.append(cls.create(**row))
                return output
        except (FileNotFoundError):
            return output

    @staticmethod
    def random_color():
        """Return a random color."""
        red = random.randint(0, 255)
        green = random.randint(0, 255)
        blue = random.randint(0, 255)
        return f"#{red:02x}{green:02x}{blue:02x}"

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws a rectangle with given width, height, and color using Turtle.
        """
        list_rectangles = [] if not list_rectangles else list_rectangles
        list_squares = [] if not list_squares else list_squares
        list_rectangles.extend(list_squares)
        total_width = 0
        for rec in list_rectangles:
            total_width += rec.width + 2
        turtle.penup()
        turtle.backward(total_width/2)
        for rec in list_rectangles:
            turtle.pendown()
            turtle.fillcolor(Base.random_color())
            turtle.begin_fill()
            for _ in range(2):
                turtle.forward(rec.width)
                turtle.right(90)
                turtle.forward(rec.height)
                turtle.right(90)
            turtle.end_fill()
            turtle.penup()
            turtle.forward(rec.width + 2)
        turtle.hideturtle()
        turtle.done()
