#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    c = my_list.copy()
    for i in range(len(c)):
        if c[i] % 2 == 0:
            c[i] = True
        else:
            c[i] = False
    return c
