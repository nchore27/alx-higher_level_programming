#!/usr/bin/python3
"""Defines a function"""


def read_file(filename=""):
    """Reads and outputs the contents of a file to stdout
    Args:
        filename: name of the file
    """
    with open(filename, encoding="utf8") as f:
        for line in f:
            print(line, end="")
