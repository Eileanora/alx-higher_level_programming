#!/usr/bin/python3
import sys


def print_args():
    sz = len(sys.argv) - 1

    print(f"{sz} argument{'' if sz == 1 else 's'}{'.' if sz == 0 else ':'}")
    for i in range(1, sz + 1):
        print(f"{i}: {sys.argv[i]}")


if __name__ == "__main__":
    print_args()
