#!/usr/bin/python3
"""Module to contain lookup function"""


class MyList(list):
    """Custom List Class with additional functions"""

    def print_sorted(self):
        """Print the list sorted in ascending order."""
        print(sorted(self))
