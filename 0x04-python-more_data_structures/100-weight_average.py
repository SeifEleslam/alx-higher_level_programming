#!/usr/bin/python3
def weight_average(my_list=[]):
    return 0 if len(my_list) == 0 else sum(map(
        lambda x: x[0]*x[1], my_list)) / sum(map(
            lambda x: x[1], my_list))
