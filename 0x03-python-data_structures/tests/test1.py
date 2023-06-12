#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx = int(input("Please input the index of element you want to retrieve: "))
def element_at(my_list, idx):
    if (idx < 0):
        return "None"
    elif (idx > len(my_list)):
        return "None"
    else:
        print("Element at index {:d} is {}".format(idx, my_list[idx]))

element_at(my_list, idx)
