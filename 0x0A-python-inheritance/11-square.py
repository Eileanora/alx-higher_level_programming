#!/usr/bin/python3
'''Module that contains the square class'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class that represents a square'''
    def __init__(self, size):
        '''Constructor'''
        self.integer_validator('size', size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        '''Returns the area of the square'''
        return self.__size * self.__size

    def __str__(self):
        '''Returns the string representation of the square'''
        return '[Square] {}/{}'.format(self.__size, self.__size)
