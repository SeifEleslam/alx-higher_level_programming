#!/usr/bin/python3
"""Pascal Module"""


def pascal_triangle(n):
    """Pascal Triangle func"""
    triangle = []
    for i in range(n):
        row = [1]
        for c in range(1, i):
            row.append(triangle[-1][c] + triangle[-1][c-1])
        if i > 0:
            row.append(1)
        triangle.append(row)
    return triangle
