#!/usr/bin/python3
"""define a function append_after"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a line of text to a file each
    line containing a matching string
    Args:
        filename: file to append to
        search_string: matching string
        new_string: text to append
    """
    text = ""
    with open(filename) as f:
        for line in f:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as g:
        g.write(text)
