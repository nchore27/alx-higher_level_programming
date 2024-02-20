#!/usr/bin/python3
"""defines square the inherits a rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """inherits from the rectangle"""
    def __init__(self, size):
        """initializes the square
        Args:
            size: size of the square
        """
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """calculates the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """prints info about the square"""
        string = type(self).__name__
        return "[{}] {:d}/{:d}".format(string, self.__size, self.__size)
