#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys


def main():
    sz = len(sys.argv)

    # if args != 3
    if sz != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # check operators
    op = ['+', '-', '*', '/']
    word = [add, sub, mul, div]
    ok = 0
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    ans = 0
    for i in range(4):
        if sys.argv[2] == op[i]:
            ans = word[i](a, b)
            ok = 1
            break

    if not ok:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    print(f"{a} {sys.argv[2]} {b} = {ans}")


if __name__ == "__main__":
    main()
