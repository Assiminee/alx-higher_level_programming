#!/usr/bin/python3
"""
matrix division module
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix that's the result of all
    the elements of "matrix" divided by "div"
    """
    if not isinstance(matrix, list) or not len(matrix) or\
       not all(isinstance(row, list) for row in matrix) or\
       not all(len(row) != 0 for row in matrix) or\
       not all(isinstance(ele, (int, float)) for row in matrix for ele in row):
        raise TypeError("matrix must be a matrix "
                        "(list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(ele / div, 2) for ele in row] for row in matrix]
