#!/usr/bin/python3
def max_integer(my_list=[]):
    max_int = None
    for num in my_list:
        if max_int == None or num > max_int:
            max_int = num
    return max_int
