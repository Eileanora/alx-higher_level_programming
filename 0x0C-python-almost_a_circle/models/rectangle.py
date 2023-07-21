#!/usr/bin/python3
"""This module contains the class Rectangle which inherits from Base"""
from models.base import Base
# from base import Base


class Rectangle(Base):
    """Definition of rectangle class"""
    def __init__(self, width=0, height=0, x=0, y=0, id=None):
        """constructor of the rect class"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """getter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """getter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """method that returns the area of the rectangle"""
        return self.width * self.height

    def display(self):
        """prints in stdout the Rectangle with # without regarding x and y"""
        # do the x and y then print the rectangle
        for i in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}" \
            .format(self.id, self.x, self.y, self.width, self.height)

# if __name__ == "__main__":
#     r1 = Rectangle(4, 6)
#     r1.display()

#     print("---")

#     r1 = Rectangle(2, 2)
#     r1.display()
