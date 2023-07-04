#!/usr/bin/python3
"""Module that prints a square with the character #."""


def print_square(size):
    """Function that prints square with the character #."""

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) is not int or size is None:
        raise TypeError("size must be an integer")

    if size < 0:
        raise TypeError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
