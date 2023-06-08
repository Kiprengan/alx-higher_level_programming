#!/usr/bin/python3
if __name__ == "__main__":
    """importing add, div, subtraction and  multiplication from multiplication"""
    from calculator_1 import sub, mul, add, div
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, add(a, b)))
    print("{} / {} = {}".format(a, b, div(a, b)))
    print("{} - {} = {}".format(a, b, sub(a, b)))
    print("{} * {} = {}".format(a, b, mul(a, b)))
