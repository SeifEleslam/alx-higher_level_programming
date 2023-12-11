#!/usr/bin/python3
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):

    def test_init(self):
        """Test valid initialization of a square"""
        square = Square(10)
        self.assertEqual(square.width, 10)
        self.assertEqual(square.height, 10)
        self.assertEqual(square.x, 0)
        self.assertEqual(square.y, 0)

    def test_init_with_position(self):
        """Test initialization with position"""
        square = Square(5, 3, 2)
        self.assertEqual(square.width, 5)
        self.assertEqual(square.height, 5)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 2)

    def test_size_property(self):
        """Test size property getter and setter"""
        square = Square(10)
        self.assertEqual(square.size, 10)
        square.size = 15
        self.assertEqual(square.size, 15)
        self.assertEqual(square.width, 15)
        self.assertEqual(square.height, 15)

    def test_update_with_positional_args(self):
        """Test update method with positional arguments"""
        square = Square(10)
        square.update(2, 15, 3, 5)
        self.assertEqual(square.id, 2)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 3)
        self.assertEqual(square.y, 5)

    def test_update_with_keyword_args(self):
        """Test update method with keyword arguments"""
        square = Square(10)
        square.update(id=3, size=20)
        self.assertEqual(square.id, 3)
        self.assertEqual(square.size, 20)

    def test_to_dictionary(self):
        """Test to_dictionary method"""
        square = Square(10, 3, 2, 3)
        dictionary = square.to_dictionary()
        self.assertEqual(dictionary["id"], 3)
        self.assertEqual(dictionary["size"], 10)
        self.assertEqual(dictionary["x"], 3)
        self.assertEqual(dictionary["y"], 2)
