#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = [0, 0]
    for i in range(2):
        if i < len(tuple_a):
            new_tuple[i] += tuple_a[i]
        if i < len(tuple_b):
            new_tuple[i] += tuple_b[i]
    return tuple(new_tuple)
