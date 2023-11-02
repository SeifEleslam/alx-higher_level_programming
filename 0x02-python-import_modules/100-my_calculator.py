#!/usr/bin/python3
from calculator_1 import add, mul, sub, div
from sys import argv

calc_map = {
    "+": add,
    "*": mul,
    "-": sub,
    "/": div
}

if __name__ == "__main__":
    args = len(argv)
    operators = ['+', '-', '*', '/']
    if (args != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    elif (not (argv[2] in operators)):
        print("Unknown operator. Available operators: +, -, * and /")
    else:
        a = int(argv[1])
        b = int(argv[3])
        print("{:d} {:s} {:d} = {:d}".format(
            a, argv[2], b, calc_map[argv[2]](a, b)))
