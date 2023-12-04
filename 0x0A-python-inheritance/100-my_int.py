#!/usr/bin/python3
"""Module to contain custom int class"""


class MyInt(int):
    """Int Class"""

    def __eq__(self, __value: object) -> bool:
        return super().__ne__(__value)

    def __ne__(self, __value: object) -> bool:
        return super().__eq__(__value)
