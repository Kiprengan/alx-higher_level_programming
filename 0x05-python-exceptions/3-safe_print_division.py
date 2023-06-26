#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        divizion = a / b
    except (TypeError, ZeroDivisionError):
        divizion = None
    finally:
        print("Inside result: {}".format(divizion))
    return (divizion)
