#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_list = [False] * len(my_list)
    for i, num in enumerate(my_list):
        if num % 2 == 0:
            divisible_list[i] = True
    return divisible_list
