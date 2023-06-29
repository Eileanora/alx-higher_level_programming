#!/usr/bin/python3
"""3-square.py: Defines class with method to calculate area"""


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
