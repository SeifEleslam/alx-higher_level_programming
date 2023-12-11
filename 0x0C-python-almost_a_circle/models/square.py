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
        """String representation"""
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


# list_rectangles = [Rectangle(100, 40), Rectangle(
#     90, 110, 30, 10), Rectangle(20, 25, 110, 80)]
# list_squares = [Square(35), Square(15, 70, 50), Square(80, 30, 70)]

# Base.draw(list_rectangles, None)
