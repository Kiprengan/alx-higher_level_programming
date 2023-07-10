#!/usr/bin/python3
"""definition of lookup function"""


def lookup(obj):
    """using dir to return list of objects and instances of obj"""
    r = dir(obj)
    return(r)
