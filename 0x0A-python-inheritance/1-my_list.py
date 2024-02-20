#!/usr/bin/python3
"""Defines subclass MyList"""


class MyList(list):
    """Inherits from list"""
    def print_sorted(self):
        """prints a sorted list"""
        print("{}".format(sorted(self)))
