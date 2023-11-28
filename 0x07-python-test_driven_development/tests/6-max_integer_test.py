#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2]), 2)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer(["1", "2D", "22.2", "23"]), "2D")
        self.assertEqual(max_integer(["1", "2", "22.2", "23"]), "23")
        with self.assertRaises(TypeError):
            self.assertEqual(max_integer([1, 2, "Sad", 4]), "sad")
            self.assertEqual(max_integer([1, 2, "Sad", [1, 2, 3]]), "sad")
            self.assertEqual(max_integer([1, (1, 2), "Sad", 4]), "sad")
