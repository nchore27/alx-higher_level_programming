#!/usr/bin/python3
"""defines a function write_file"""


def write_file(filename="", text=""):
    """Writes a string to a file and returns the number of characters
    Args:
        filename: file to write to
        text: string to write
    Return: No. of chars written
    """
    with open(filename, 'w', encoding="utf8") as f:
        return f.write(text)
