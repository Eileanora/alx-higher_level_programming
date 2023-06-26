#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except Exception:
                pass
    except IndexError:
        pass
    finally:
        if count!=0:
            print()
        return count
