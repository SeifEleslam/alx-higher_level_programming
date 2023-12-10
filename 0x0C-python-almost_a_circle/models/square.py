"""Square Class"""
from rectangle import Rectangle
from base import Base


class Square(Rectangle):
    """Square Class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize Square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        return "[{}] ({}) {}/{} - {}".format(
            self.__class__.__name__, self.id, self.x, self.y, self.size)

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        super().__setattr__("width", value)
        super().__setattr__("height", value)
        self.__size = value

    def update(self, *args, **kwargs):
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


r1 = Rectangle(3, 5, 1)
r1_dictionary = r1.to_dictionary()
r2 = Rectangle.create(**r1_dictionary)
print(r1)
print(r2)
print(r1 is r2)
print(r1 == r2)
