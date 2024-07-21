#!/usr/bin/python3
"""Inherits a square from a rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square"""
    def __init__(self, size, x=0, y=0, id=None):
        """initializes a square using rectangle"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """prints info about square"""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__,
                                             self.id,
                                             self.x,
                                             self.y,
                                             self.width)

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, size):
        """size setter"""
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """updates attributes to args and kwargs"""
        if len(args) > 0:
            for i, m in enumerate(args):
                if i == 0:
                    self.id = m
                if i == 1:
                    self.size = m
                if i == 2:
                    self.x = m
                if i == 3:
                    self.y = m
        elif len(kwargs) > 0:
            for j, k in kwargs.items():
                if j == "id":
                    self.id = k
                if j == "size":
                    self.size = k
                if j == "x":
                    self.x = k
                if j == "y":
                    self.y = k

    def to_dictionary(self):
        """prints the dictionary representation of the square"""
        obj = {}
        for i in ['id', 'size', 'x', 'y']:
            obj[i] = getattr(self, i)
        return obj
