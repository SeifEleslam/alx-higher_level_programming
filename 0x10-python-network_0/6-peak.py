#!/usr/bin/python3
"""Find peak module"""


def rec_peak(arr, low, high):
    """Recursive function to find the peak"""
    if low == high:
        return arr[low]
    if low + 1 == high:
        return max(arr[low], arr[high])
    mid = int((high + low)/2)
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return arr[mid]
    if arr[mid] > arr[mid + 1]:
        return rec_peak(arr, low, mid - 1)
    return rec_peak(arr, mid + 1, high)


def find_peak(list_of_integers):
    """Finds the peak element in a list"""
    list_len = len(list_of_integers)
    if list_len == 0:
        return None
    return rec_peak(list_of_integers, 0, list_len - 1)
