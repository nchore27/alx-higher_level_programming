#!/usr/bin/python3
"""defines a function append_write"""


def append_write(filename="", text=""):
    """appends string to text file
    Args:
        filename: name of file to append to
        text: string to append
    Return: No. of printed chars
    """
    with open(filename, 'a', encoding="utf8") as f:
        return f.write(text)
