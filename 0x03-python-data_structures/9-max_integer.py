#!/usr/bin/python3
def max_integer(my_list=[]):
    cnt = len(my_list)
    if cnt == 0:
        return None
    d_max = my_list[0]
    for a in my_list:
        if a > d_max:
            d_max = a
    return d_max
