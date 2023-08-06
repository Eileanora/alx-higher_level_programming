#!/usr/bin/python3
'''Module that defines a Student class'''


class Student:
    '''class that defines a student'''
    def __init__(self, first_name, last_name, age):
        '''Initializes a student'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Returns the dictionary representation of a Student instance'''
        return self.__dict__
