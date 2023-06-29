#!/usr/bin/python3
"""6-square.py: Defines size and position attributes
for Square class and methods for printing the square"""


class Square:
    """Creates square type"""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square with size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Defines size of Square and returns its value"""
        return self.__size

    @size.setter
    def size(self, value):
        """Defines the value of size of Square and checks for errors"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """Defines position of Square and returns its value"""
        return self.__position

    @position.setter
    def position(self, value):
        """Defines the value of position of Square and checks for errors"""
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or type(value[1]) is not int or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the area of Square"""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for j in range(self.size):
                print("{}{}".format(" " * self.__position[0], "#" * self.size))
