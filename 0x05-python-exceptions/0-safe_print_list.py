#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    item = 0
    for m in range(x):
        try:
            print("{}".format(my_list[m]), end="")
            item += 1
        except IndexError:
            break
    print("")
    return (item)
