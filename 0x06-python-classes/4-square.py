#!/usr/bin/python3
"""4-square.py: Defines class with
setter and getter methods for size attribute"""


class Square:
    """Creates square type"""

    def __init__(self, size=0):
        """Initializes Square with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """Returns the current square size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the square size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        self.__size = value
