#!/usr/bin/python3
"""Creating Mylist class which inherits list"""


class MyList(list):
    """MyList class methods"""
    def __init__(self):
        """Initiaization"""
        super().__init__()

    def print_sorted(self):
        """Method that sorts list and prints"""
        print(sorted(self))
