#!/usr/bin/python3
'''Module for to_json_string method.'''
import json


def to_json_string(my_obj):
    '''Method for returning JSON representation of an object (string).'''
    return json.dumps(my_obj)
