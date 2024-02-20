#!/usr/bin/python3
"""defines a class MyInt"""


class MyInt(int):
    """Inherits from int"""
    def __ne__(self, n):
        """Returns False for True"""
        return super().__eq__(n)

    def __eq__(self, n):
        """Returns True for False"""
        return super().__ne__(n)
