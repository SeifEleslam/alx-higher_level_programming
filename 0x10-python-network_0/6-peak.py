#!/usr/bin/python3

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


# Testing the function with various inputs
print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
