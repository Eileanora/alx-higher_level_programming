#!/usr/bin/python3
'''Module that contais the following:
    is_same_class(obj, a_class) - checks if obj is an instance of a_class
'''


def is_same_class(obj, a_class):
    ''''Function that checks if obj is an instance of a_class'''
    return type(obj) == a_class
