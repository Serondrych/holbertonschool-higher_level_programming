#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    c = my_list.copy()
    c.sort()
    return c[-1]
