#!/usr/bin/python3
"""defines a function"""


def is_same_class(obj, a_class):
    """returns true if obj is an instance of a_class
    Args:
        obj: object
        a_class: class
    """
    if type(obj) == a_class:
        return True
    return False
