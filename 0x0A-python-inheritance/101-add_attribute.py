#!/usr/bin/python3
"""defines a function"""


def add_attribute(obj, attr, value):
    """Adds new attribute to an object when possible
    Args:
        obj: object
        attr: attribute
        value: value
    Raises:
        TypeError: if impossible
    """
    if hasattr(obj, "__dict__"):
        setattr(obj, attr, value)
    else:
        raise TypeError('can\'t add new attribute')
