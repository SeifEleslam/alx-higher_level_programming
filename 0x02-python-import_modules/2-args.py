#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    print("{:d} argument{:s}".format(len(argv) - 1, ":" if len(argv)
          == 2 else ("s." if len(argv) == 1 else "s:")))
    for i in range(len(argv) - 1):
        print("{:d}: {:s}".format(i+1, argv[i+1]))
