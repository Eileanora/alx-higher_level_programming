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

    def test_Raises(self):
        """Test raises"""
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, "String")
        self.assertRaises(TypeError, max_integer, (1, 2, 3))
        self.assertRaises(TypeError, max_integer, {1, 2, 3})
        self.assertRaises(TypeError, max_integer, {1: 2, 3: 4})
        self.assertRaises(TypeError, max_integer, float('nan'))
        self.assertRaises(TypeError, max_integer, float('inf'))
        self.assertRaises(TypeError, max_integer, 1, 2)

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

    def test_OneElement(self):
        """Test one element"""
        self.assertEqual(max_integer([1]), 1)
