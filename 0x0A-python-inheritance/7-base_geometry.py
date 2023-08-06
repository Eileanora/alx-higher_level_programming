#!/usr/bin/python3
'''Module that contains the BaseGeometry class'''


class BaseGeometry:
    '''A base empty class'''
    def area(self):
        '''Just function that raises an excpetion because \
it is not implemented'''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        '''Function that validates value'''
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))

        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/7-base_geometry.txt')
