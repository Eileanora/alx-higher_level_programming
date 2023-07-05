#!/usr/bin/python3
"""This module contains a function that prints
My name is <first name> <last name>"""


def say_my_name(first_name="", last_name=""):
    """prints My name is <first name> <last name>"""

    if type(first_name) is not str or first_name is None:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str or last_name is None:
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))
