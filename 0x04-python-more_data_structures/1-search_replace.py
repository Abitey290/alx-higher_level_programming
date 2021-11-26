#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = my_list.copy()
    for a, b in enumerate(new):
        if b == search:
            new[a] = replace
    return new
