#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Finds the peak element in a list"""
    list_len = len(list_of_integers)
    if list_len == 0:
        return None
    if list_len == 1:
        return list_of_integers[0]
    if list_len == 2:
        return max(list_of_integers[0],
                   list_of_integers[1])
    target = int(list_len/2)
    if list_of_integers[target] > list_of_integers[target+1] and\
            list_of_integers[target] > list_of_integers[target-1]:
        return list_of_integers[target]
    if list_of_integers[target] > list_of_integers[target+1]:
        return find_peak(list_of_integers[:target])
    return find_peak(list_of_integers[target+1:])
