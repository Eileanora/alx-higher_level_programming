#!/usr/bin/python3
"""This module contains a function that tests the max_integer function"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestAddInteger(unittest.TestCase):
    """Class that contains the test functions"""

    def test_docstring(self):
        """Test docstring"""
        self.assertIsNotNone(max_integer.__doc__)
        self.assertTrue(len(max_integer.__doc__) > 1)
        # check module docstring
        self.assertIsNotNone(__import__('6-max_integer').__doc__)
        self.assertTrue(len(__import__('6-max_integer').__doc__) > 1)

        list_input = [1, 2, 3, "String"]
        with self.assertRaises(TypeError):
            max_integer(list_input)

    def test_Empty(self):
        """Test empty"""
        self.assertEqual(max_integer([]), None)

    def test_Regular(self):
        """Test regular"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([-6, -2, -1, -96]), -1)
        self.assertEqual(max_integer([1, 2, -3, 4]), 4)

    def test_one_element(self):
        """Test one element"""
        self.assertEqual(max_integer([1]), 1)

    def test_max_at_beginning(self):
        """Test max at beginning"""
        self.assertEqual(max_integer([10, 2, 3, 4]), 10)

    def test_max_at_middle(self):
        """Test max at middle"""
        self.assertEqual(max_integer([1, 2, 10, 4]), 10)

    def test_max_at_end(self):
        """Test max at end"""
        self.assertEqual(max_integer([1, 2, 3, 10]), 10)
