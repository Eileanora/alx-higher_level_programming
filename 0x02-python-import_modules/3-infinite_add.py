#!/usr/bin/python3
import sys


def inf_add():
    sz = len(sys.argv)
    sum = 0
    for i in range(1, sz):
        sum += int(sys.argv[i])
    print(sum)


if __name__ == "__main__":
    inf_add()
