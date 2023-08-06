#!#!/usr/bin/python3
'''Module that contains the MyInt class'''


class MyInt(int):
    '''Class that represents an integer'''
    def __eq__(self, other):
        '''Returns the opposite of the equal operator'''
        return super().__ne__(other)

    def __ne__(self, other):
        '''Returns the opposite of the not equal operator'''
        return super().__eq__(other)
