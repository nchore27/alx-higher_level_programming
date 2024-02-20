#!/usr/bin/python3
"""defines a function"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class inherited
    (inderectly or directly) from the specified class: otherwise false
    Args:
        obj: object
        a_class: class
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
