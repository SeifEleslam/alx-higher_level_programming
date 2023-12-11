#!/usr/bin/python3
"""Square Class Module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """String representation"""
        return "[{}] ({}) {}/{} - {}".format(
            type(self).__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.width

    @size.setter
    def size(self, size):
        """Setter for size"""
        self.width = size
        self.height = size
        # self.__size = size

    def update(self, *args, **kwargs):
        """Update square attributes"""
        if len(args) > 1:
            args = list(args)
            args.insert(1, args[1])
            args = tuple(args)
        elif kwargs.get("size"):
            kwargs['width'] = kwargs["size"]
            kwargs["height"] = kwargs["size"]
            del kwargs["size"]
        super().update(*args, **kwargs)
        self.size = super().width

    def to_dictionary(self):
        """Return a dictionary representation of the square."""
        newDic = {}
        for key, val in vars(self).items():
            if "width" not in key and "height" not in key:
                newDic[key.replace("_", "").replace(
                    "Rectangle", "").replace("Square", "")] = val
        return newDic
