#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    uniq_sum = 0
    for i in my_list:
        if i not in seen:
            uniq_sum += i
            seen.add(i)
    return uniq_sum
