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
        super().integer_validator("height", height)
        self.__height = height
        super().integer_validator("width", width)
        self.__width = width

    def area(self):
        """calculates the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """prints info about the rectangle"""
        string = type(self).__name__
        return "[{}] {}/{}".format(string, str(self.__width),
                                   str(self.__height))
