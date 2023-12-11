from models.base import Base
from models.rectangle import Rectangle
import unittest
from unittest.mock import Mock, patch
import json


class TestBase(unittest.TestCase):

    def test_init(self):
        """Test initialization of Base object."""
        base_obj = Base()
        self.assertIsNotNone(base_obj.id)
        self.assertEqual(base_obj.id, 1)

        base_obj_with_id = Base(10)
        self.assertEqual(base_obj_with_id.id, 10)

    def test_to_json_string(self):
        """Test conversion of list of dictionaries to JSON string."""
        list_dicts = [{"id": 1}, {"id": 2}]
        json_string = Base.to_json_string(list_dicts)
        self.assertEqual(json_string, '[{"id": 1}, {"id": 2}]')
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_from_json_string(self):
        """Test conversion of JSON string to list of dictionaries."""
        json_string = '[{"id": 1}, {"id": 2}]'
        list_dicts = Base.from_json_string(json_string)
        self.assertEqual(list_dicts, [{"id": 1}, {"id": 2}])
        self.assertEqual(Base.from_json_string(None), [])

    def test_get_heads(self):
        """Test retrieval of object heads based on class name."""
        self.assertEqual(Base.get_heads(), ["id", "width", "height", "x", "y"])
        rectangle_heads = Base.get_heads(Rectangle)
        self.assertEqual(rectangle_heads, ["id", "width", "height", "x", "y"])

    def test_save_to_file(self):
        """Test saving list of objects to a JSON file."""
        with patch("builtins.open"):
            Base.save_to_file([Base(1), Base(2)])
            open.assert_called_once_with("Base.json", "w")

    def test_create(self):
        """Test creation of object from a dictionary."""
        rectangle = Rectangle.create(width=10, height=20, x=100, y=200)
        self.assertEqual(rectangle.width, 10)
        self.assertEqual(rectangle.height, 20)
        self.assertEqual(rectangle.x, 100)
        self.assertEqual(rectangle.y, 200)

    def test_load_from_file(self):
        """Test loading list of objects from a JSON file."""
        test_rec = Rectangle(1, 2)
        with patch("builtins.open") as mock_open:
            mock_open.return_value = Mock(
                read=Mock(return_value=Base.to_json_string([test_rec.to_dictionary()])))
            objects = test_rec.load_from_file()
            self.assertEqual(objects, [test_rec.to_dictionary()])

    def test_save_to_file_csv(self):
        """Test saving list of objects to a CSV file."""
        with patch("builtins.open"):
            Base.save_to_file_csv([Base(1), Base(2)])
            open.assert_called_once_with("Base.csv", "w")

    def test_load_from_file_csv(self):
        """Test loading list of objects from a CSV file."""
        test_rec = Rectangle(1, 2)
        with patch("builtins.open") as mock_open:
            mock_open.return_value = Mock(
                read=Mock(return_value="id\n1\n2\n"))
            objects = test_rec.load_from_file_csv()
            self.assertEqual(objects, [])

    def test_random_color(self):
        """Test generation of random color."""
        color = Base.random_color()
        self.assertRegex(color, r"^#[0-9a-f]{6}$")
