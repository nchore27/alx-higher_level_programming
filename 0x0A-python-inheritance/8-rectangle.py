#!/usr/bin/python3
"""Defines an inheritant class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represent rectangle inheriting BaseGeometry"""
    def __init__(self, width, height):
        """initialize a rectangle
        Args:
            width: rectangle width
            height: rectangle height
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
