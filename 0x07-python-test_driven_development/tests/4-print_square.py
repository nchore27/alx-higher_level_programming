#!/usr/bin/python3
"""Defines a function that prints a square"""


def print_square(size):
    """prints a square with the character #
    Args:
        @size: the size of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for num in range(size):
        print("#" * size)
