#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    item = 0
    for m in range(0, x):
        try:
            print("{:d}".format(my_list[m]), end="")
            item += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (item)
