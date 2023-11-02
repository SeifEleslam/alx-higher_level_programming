#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    a = 0
    b = 1
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c = add(c, i)
        return c
    return sub(a, b)
