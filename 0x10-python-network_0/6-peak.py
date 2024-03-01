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
    if list_of_integers[target] < list_of_integers[target-1]:
        r_list = list_of_integers[:target]
    r_list = list_of_integers[target+1:]
    # Check if there is only one
    # for i in range(list_len):
    #     peak = list_of_integers[i]
    #     if i+1 < list_len and\
    #             list_of_integers[i] > list_of_integers[i+1]:
    #         break
    return find_peak(r_list)


print(find_peak([1, 2, 4, 6, 3]))
print(find_peak([4, 2, 1, 2, 3, 1]))
print(find_peak([2, 2, 2]))
print(find_peak([]))
print(find_peak([-2, -4, 2, 1]))
print(find_peak([4, 2, 1, 2, 2, 2, 3, 1]))
