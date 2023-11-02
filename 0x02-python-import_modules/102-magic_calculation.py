#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    a = 0
    b = 1
    if b < a:
        c = add(b, a)
        for i in range(4, 6):
            c = add(i, c)
        return c
    return sub(b, a)
