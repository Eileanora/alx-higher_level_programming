#!/usr/bin/python3
'''Module that defines a Student class'''


class Student:
    '''class that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''Initializes a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''Returns the dictionary representation of a Student instance'''
        if attrs is None:
            return self.__dict__

        new_dict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                new_dict[key] = value
        return new_dict
