#!/usr/bin/python3
def search_replace(my_list, search, replace):
    c = my_list.copy()
    for i in range(len(c)):
        if c[i] == search:
            c[i] = replace
    return c
