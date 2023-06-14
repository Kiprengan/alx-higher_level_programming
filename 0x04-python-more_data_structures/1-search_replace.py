#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_lst = []
    for m in my_list:
        if m == search:
            new_lst.append(replace)
        else:
            new_lst.append(m)
    return new_lst
