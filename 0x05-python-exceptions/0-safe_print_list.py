#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    printedElements = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            printedElements += 1
        except (KeyError, Exception):
            break

    print()
    return printedElements
