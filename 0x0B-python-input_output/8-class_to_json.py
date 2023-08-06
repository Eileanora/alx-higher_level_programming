#!/usr/bin/python3
'''Module that returns the dictionary description with simple data structure'''


def class_to_json(obj):
    '''Returns the dictionary description with simple data structure'''
    return obj.__dict__
