#!/usr/bin/python3
"""Matrix Division Module"""


def matrix_divided(matrix, div):
    """Matrix Division by num function"""
    rowlen = len(matrix[0])
    typeErrMsg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or not len(matrix):
        raise TypeError(typeErrMsg)
    for row in matrix:
        if not isinstance(row, list) or not rowlen:
            raise TypeError(typeErrMsg)
        if not (len(row) == rowlen):
            raise TypeError("Each row of the matrix must have the same size")
        for n in row:
            if not isinstance(n, float) and not isinstance(n, int):
                raise TypeError(typeErrMsg)
    if not isinstance(div, float) and not isinstance(div, int):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    retunredMatrix = []
    for row in matrix:
        newRow = [round(x / div, 2) for x in row]
        retunredMatrix.append(newRow)
    return retunredMatrix
