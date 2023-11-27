#!/usr/bin/python3
import sys


def safe_pos(x, y, poss):
    for pos in poss:
        if pos[0] == x or pos[1] == y or abs(pos[0]-x) == abs(pos[1]-y):
            return False
    return True


def queen_pos(n, row, poss):
    if row > n-1:
        print(poss)
        return
    for i in range(n):
        tmp = poss[:]
        if safe_pos(row, i, tmp):
            tmp.append([row, i])
            queen_pos(n, row+1, tmp)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if (N < 4):
        print("N must be at least 4")
        sys.exit(1)
    queen_pos(N, 0, [])
