#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        print("{}".format(a/b))
        result = a/b
    except (TypeError, ZeroDivisionError):
        pass
    return result
