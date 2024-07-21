#!/usr/bin/python3
""" divides a matrix and returns the quotient matrix"""


def matrix_divided(matrix, div):
    """Divides the contents of a matrix
    Args:
        @matrix: matrix
        @div: integer to use
    """
    for i in matrix:
        for j in i:
            if type(j) is not int and type(j) is not float:
                raise TypeError("matrix must be a matrix (list \
of lists) of integers/floats")
    for m in matrix:
        if not (len(m) == len(matrix[0])):
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    quotient = [[eval("{:.2f}".format(i / div)) for i in j]
                for j in matrix]
    return quotient
