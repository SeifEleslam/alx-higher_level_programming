#!/usr/bin/python3
"""Matrix Division Module"""
import numpy as np


def check_matrix(name, matrix):
    """Check if the given matrix is valid."""
    if not isinstance(matrix, list):
        raise TypeError("{} must be a list".format(name))
    if not len(matrix) or (isinstance(matrix[0], list) and not len(matrix[0])):
        raise ValueError("{} can't be empty".format(name))
    rowlen = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("{} must be a list of lists".format(name))
        if not (len(row) == rowlen):
            raise TypeError(
                "each row of {} must be of the same size".format(name))
        for n in row:
            if not isinstance(n, float) and not isinstance(n, int):
                raise TypeError(
                    "{} should contain only integers or floats".format(name))


def lazy_matrix_mul(m_a, m_b):
    return np.matmul(m_a, m_b)


# print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# print(matrix_mul([], [1, 2]))
