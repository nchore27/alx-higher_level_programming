#!/usr/bin/python3
# add_integer.py


"""Contains only one function, def add_integer(a, b=98):"""


def add_integer(a, b=98):
    """Adds and returns the sum of two integers
    Args:
        a: first integer
        b: second integer
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    if type(a) is float or type(b) is float:
        a = int(a)
        b = int(b)
    return a + b
