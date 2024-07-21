#!/usr/bin/python3
"""defines a function that prints your name"""


def say_my_name(first_name, last_name=""):
    """Prints my name is <first name> <last name>
    Args:
        @first_name: first name of the person
        @last_name: surname of the person
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print('My name is {:s} {:s}'.format(first_name, last_name))
