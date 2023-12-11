#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle

# Test class initialization with valid and invalid values


class TestRectangleInit(unittest.TestCase):
    def test_init_valid_values(self):
        """Test initialization with valid width, height, x, and y."""
        rectangle = Rectangle(10, 20, 5, 7)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 7)

    def test_init_invalid_width_type(self):
        """Test initialization with invalid width type."""
        self.assertRaises(TypeError, Rectangle, "10", 20, 5, 7)

    def test_init_negative_width(self):
        """Test initialization with negative width."""
        self.assertRaises(ValueError, Rectangle, -10, 20, 5, 7)

    def test_init_invalid_height_type(self):
        """Test initialization with invalid height type."""
        self.assertRaises(TypeError, Rectangle, 10, "20", 5, 7)

    def test_init_negative_height(self):
        """Test initialization with negative height."""
        self.assertRaises(ValueError, Rectangle, 10, -20, 5, 7)

    def test_init_invalid_x_type(self):
        """Test initialization with invalid x type."""
        self.assertRaises(TypeError, Rectangle, 10, 20, "5", 7)

    def test_init_negative_x(self):
        """Test initialization with negative x."""
        self.assertRaises(ValueError, Rectangle, 10, 20, -5, 7)

    def test_init_invalid_y_type(self):
        """Test initialization with invalid y type."""
        self.assertRaises(TypeError, Rectangle, 10, 20, 5, "7")

    def test_init_negative_y(self):
        """Test initialization with negative y."""
        self.assertRaises(ValueError, Rectangle, 10, 20, 5, -7)

# Test accessor and setter methods


class TestRectangleAccessors(unittest.TestCase):
    def test_width_setter(self):
        """Test setting width with valid and invalid values."""
        rectangle = Rectangle(10, 20)
        rectangle.width = 15
        self.assertEqual(rectangle.width, 15)
        self.assertRaises(TypeError, setattr, rectangle, "width", "10")
        self.assertRaises(ValueError, setattr, rectangle, "width", -10)

    def test_height_setter(self):
        """Test setting height with valid and invalid values."""
        rectangle = Rectangle(10, 20)
        rectangle.height = 25
        self.assertEqual(rectangle.height, 25)
        self.assertRaises(TypeError, setattr, rectangle, "height", "20")
        self.assertRaises(ValueError, setattr, rectangle, "height", -20)

    def test_x_setter(self):
        """Test setting x with valid and invalid values."""
        rectangle = Rectangle(10, 20)
        rectangle.x = 3
        self.assertEqual(rectangle.x, 3)
        self.assertRaises(TypeError, setattr, rectangle, "x", "3")
        self.assertRaises(ValueError, setattr, rectangle, "x", -3)

    def test_y_setter(self):
        """Test setting y with valid and invalid values."""
        rectangle = Rectangle(10, 20)
        rectangle.y = 4
        self.assertEqual(rectangle.y, 4)
        self.assertRaises(TypeError, setattr, rectangle, "y", "4")
        self.assertRaises(ValueError, setattr, rectangle, "y", -4)

# Test other methods


class TestRectangleOtherMethods(unittest.TestCase):
    def test_update(self):
        """Test update method with positional and keyword arguments."""
        rectangle = Rectangle(10, 20)
        rectangle.update(2, 15, 3, 5)
        self.assertEqual(rectangle.id, 2)
