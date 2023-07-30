#!/usr/bin/python3
'''
Module that contais the following:
    inherits_from(obj, a_class) - checks if obj is an instance of a_class
'''


def inherits_from(obj, a_class):
    '''Checks if the object is an instance of a class that\
        inherited (directly or indirectly) from the specified class'''
    # check if obj isn't an instance of a_class
    # and check if obj is a subclass of a_class
    return issubclass(type(obj), a_class) and type(obj) != a_class
