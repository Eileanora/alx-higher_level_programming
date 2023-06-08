#!/usr/bin/python3
import hidden_4


def print_all_names():
    for i in sorted(dir(hidden_4)):
        if i[:2] != "__":
            print(i)


if __name__ == "__main__":
    print_all_names()
