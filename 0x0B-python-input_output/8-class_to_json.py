#!/usr/bin/python3
"""Task9 Module"""
import json


def class_to_json(obj):
    return (obj.__dict__)


# class MyClass:
#     """ My class
#     """

#     def __init__(self, name):
#         self.name = name
#         self.number = 0

#     def __str__(self):
#         return "[MyClass] {} - {:d}".format(self.name, self.number)


# m = MyClass("John")
# m.number = 89
# print(type(m))
# print(m)

# mj = class_to_json(m)
# print(type(mj))
# print(mj)
