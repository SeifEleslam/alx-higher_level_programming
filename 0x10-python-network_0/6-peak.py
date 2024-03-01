#!/usr/bin/python3
"""Find peak module"""


def find_peak(list_of_integers):
    """Finds the peak element in a list"""
    peak = None
    # Check if there is only one
    for i in range(len(list_of_integers)):
        peak = list_of_integers[i]
        if i+1 < len(list_of_integers) and\
                list_of_integers[i] > list_of_integers[i+1]:
            break
    return peak
