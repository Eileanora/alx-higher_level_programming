#!/usr/bin/python3
"""2-square.py: Defines class with size attribute and checks for errors"""


class square:
    """Creates square type"""

    def __init__(self, size=0):
        """Initializes Square with size"""
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
