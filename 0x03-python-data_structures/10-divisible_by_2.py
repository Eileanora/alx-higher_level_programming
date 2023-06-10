#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    ans = []
    for i in range(0, len(my_list)):
        if my_list[i] % 2 == 0:
            ans.append(True)
        else:
            ans.append(False)
    return ans
