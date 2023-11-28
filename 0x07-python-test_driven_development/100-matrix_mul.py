#!/usr/bin/python3
"""Matrix Division Module"""


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


def matrix_mul(m_a, m_b):
    """Matrix Division by num function"""
    check_matrix("m_a", m_a)
    check_matrix("m_b", m_b)
    if not (len(m_a[0]) == len(m_b)):
        raise ValueError("m_a and m_b can't be multiplied")
    returnedMatrx = []
    for i in range(len(m_a)):
        newRow = []
        for n in range(len(m_b[0])):
            sum = 0
            for s in range(len(m_a[0])):
                sum += m_a[i][s] * m_b[s][n]
            newRow.append(sum)
        returnedMatrx.append(newRow)
    return returnedMatrx


# print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
# print(matrix_mul([[5], [5]], [[6, 2], [11, 11]]))
