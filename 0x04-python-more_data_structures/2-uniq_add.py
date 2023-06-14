#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    my_list = list(set(my_list))
    for m in my_list:
        total += m
    return total
