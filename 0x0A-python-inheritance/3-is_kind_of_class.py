#!/usr/bin/python3
"""defines a function"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is an instance of or if the object
    is an instance of a class that inherited from the specified class
    otherwise returns false
    Args:
        obj: object
        a_class: class
    """
    if type(obj) == a_class or isinstance(obj, a_class) is True:
        return True
    return False
