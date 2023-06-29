#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(int(my_list[i])), end="")
                count += 1
            except (ValueError, TypeError):
                pass
            except IndexError:
                raise IndexError
    finally:
        print()
        return count
