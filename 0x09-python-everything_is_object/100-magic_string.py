#!/usr/bin/python3
def magic_string(ls=[]):
    ls += [1]
    return "BestSchool, " * (len(ls)-1) + "BestSchool"


for i in range(10):
    print(magic_string())
