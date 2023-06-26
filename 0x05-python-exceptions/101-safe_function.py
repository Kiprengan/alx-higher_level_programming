#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        outcome = fct(*args)
        return (outcome)
    except Exception as t:
        print("Exception: {}".format(t), file=sys.stderr)
        return (None)
