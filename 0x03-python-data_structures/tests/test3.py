#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
def print_reversed(my_list=[]):
    for m in my_list:
        print("{:d}".format(my_list[-m]))
print_reversed(my_list)
