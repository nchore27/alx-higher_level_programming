#!/usr/bin/python3
"""defines a class"""


class BaseGeometry:
    """presents base geometry"""
    def area(self):
        """raise exception if not implemented"""
        raise Exception("area() is not implemented")
