#!/usr/bin/python3
'''Module that contais the following:
class MyList - inherits from list
'''


class MyList(list):
    '''Class that inherits from list'''
    def print_sorted(self):
        '''Function that returns the list, but in sorted order'''
        print(sorted(self))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
