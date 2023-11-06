#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    # if matrix:
    for row in matrix:
        for i, itm in enumerate(row):
            print("{:d}".format(itm), end=(
                '' if i+1 == len(row) else ' '))
        print()
