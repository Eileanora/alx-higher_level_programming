#!/usr/bin/python3
"""Unittest for base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Unittest class for base.py"""

    def test_given_id(self):
        """Test for given id"""
        self.assertEqual(Base(100).id, 100)
        self.assertEqual(Base(0).id, 0)
        self.assertEqual(Base(-1).id, -1)

    def test_no_id(self):
        """Test for no id"""
        self.assertEqual(Base().id, 1)
        self.assertNotEqual(Base().id, 3)
        self.assertNotEqual(Base().id, 0)
