#!/usr/bin/python3
"""Module that divides all elements of a matrix."""


def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix."""

    if type(matrix) is not list or matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of\
                         integers/floats")

    if type(div) is not int and type(div) is not float or div is None:
        raise TypeError("div must be a number")

    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of\
                             integers/floats")

    for row in matrix:
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of\
                                 integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: round(x / div, 2), row)))

    return new_matrix
