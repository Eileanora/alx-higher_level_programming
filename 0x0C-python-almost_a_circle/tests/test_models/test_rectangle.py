#!/usr/bin/python3

"""Unittest module for rectangle.py"""
import unittest
from models.rectangle import Rectangle
from models.base import Base


class TestRectangle(unittest.TestCase):
    """class contains the unittests for rectangle.py"""

    # check if the class Rectangle is inheriting from Base
    def test_inheritance(self):
        """test if Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    # check if width, height, x, y, id are private
    def test_private(self):
        """test if width, height, x, y, id are private"""
        self.assertFalse(hasattr(Rectangle, "_Rectangle__width"))
        self.assertFalse(hasattr(Rectangle, "_Rectangle__height"))
        self.assertFalse(hasattr(Rectangle, "_Rectangle__x"))
        self.assertFalse(hasattr(Rectangle, "_Rectangle__y"))
        # self.assertTrue(hasattr(Rectangle, "id")) ??? not working

    # check if width, height, x, y, id are integers
    def test_type_erros(self):
        """check if width, height, x, y are integers"""
        with self.assertRaises(TypeError):
            Rectangle("1", 2)  # width
            Rectangle(1, "2")  # height
            Rectangle(1, 2, "3")  # x
            Rectangle(1, 2, 3, "4")  # y

    def test_value_errors(self):
        """check if width, height, x, y are not negative"""
        with self.assertRaises(ValueError):
            Rectangle(0, 1)
            Rectangle(1, 0)
            Rectangle(-1, 1)
            Rectangle(1, -1)
            Rectangle(1, 1, -1)
            Rectangle(1, 1, 1, -1)

    def test_values_are_set(self):
        """check if values are correctly set"""
        r1 = Rectangle(10, 2, 4, 5, 3)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 4)
        self.assertEqual(r1.y, 5)
        self.assertEqual(r1.id, 3)
        r1.x = 0
        r1.y = 0
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

    def test_area(self):
        r1 = Rectangle(10, 3, 0, 0, 0)
        self.assertEqual(r1.width * r1.height, r1.area())
        # check for nan -> overflow

    def test_display(self):
        r1 = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(r1.display(), None)

    def test_str(self):
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), "[Rectangle] (12) 2/1 - 4/6")
