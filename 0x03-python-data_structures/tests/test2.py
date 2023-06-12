#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
idx = int(input("Please input the index of element you want to retrieve: "))
def element_at(my_list, idx):
    return(my_list[idx] if 0 <= idx < len(my_list) else "None")
element_at(my_list, idx)
