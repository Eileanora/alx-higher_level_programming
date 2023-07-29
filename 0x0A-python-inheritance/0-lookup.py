#!/usr/bin/python3
'''This module contains the following functions:
lookup(obj) - returns the list of available attributes and methods of an object
'''


def lookup(obj):
    '''Function that returns the list of available\
    attributed and methods of an object'''
    return dir(obj)
