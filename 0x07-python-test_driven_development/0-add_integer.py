#!/usr/bin/python3
"""Module for a function that adds 2 integers."""


def add_integer(a, b=98):
    """Function that adds 2 integers."""

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)
    return a + b
