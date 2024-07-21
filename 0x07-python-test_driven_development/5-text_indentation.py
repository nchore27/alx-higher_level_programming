#!/usr/bin/python3
"""Defines a function that prints a new line after the characters: ., ? and :
"""


def text_indentation(text):
    """Prints a new line after . ? and :
    Args:
        @text: the text to prints
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    indent = ''
    i = 0
    while i < len(text):
        indent += text[i]
        if text[i] in ['.', '?', ':']:
            indent = indent.strip()
            print(indent + '\n')
            try:
                if text[i + 1] == ' ':
                    i += 1
            except IndexError:
                pass
            indent = ''
        i += 1

    if len(indent) > 0:
        print(indent, end="")
