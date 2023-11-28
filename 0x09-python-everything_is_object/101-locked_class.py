#!/usr/bin/python3
"""Locked Module"""


class LockedClass:
    """Locked Class"""

    def __setattr__(self, name, value):
        """Perevent any attribute other than first_name"""
        if name != "first_name":
            raise AttributeError("'{}' object has no attribute '{}'".format(
                self.__class__.__name__, name))
        super().__setattr__(name, value)
