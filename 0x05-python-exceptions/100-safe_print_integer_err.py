#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    res = True
    try:
        print("{:d}".format(value))
    except (ValueError) as err:
        res = False
        sys.stderr.write("Exception: {}\n".format(err))
    return res
