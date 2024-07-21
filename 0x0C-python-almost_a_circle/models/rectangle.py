#!/usr/bin/python3
"""Inherits a rectangle from Base"""
from models.base import Base


class Rectangle(Base):
    """Defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle from base init"""

        # Validate width
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        # validate height
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        # validate x
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        # validate y
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """width getter function
        """

        return self.__width

    @width.setter
    def width(self, width):
        """Sets the width attribute
        """

        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """height getter function
        """

        return self.__height

    @height.setter
    def height(self, height):
        """Sets the height attribute
        """

        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter function
        """

        return self.__x

    @x.setter
    def x(self, x):
        """Sets the x attribute
        """

        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter function
        """

        return self.__y

    @y.setter
    def y(self, y):
        """Sets the x attribute
        """

        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """Retrieves the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints the rectangle to stdout using '#'"""

        if self.__width == 0 or self.__height == 0:
            print()
            return
        if self.__y != 0:
            print("\n" * (self.__y - 1))
        for i in range(self.__height):
            if self.__x != 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """Prints info about the rectangle"""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__,
                                                self.id,
                                                self.__x,
                                                self.__y,
                                                self.__width,
                                                self.__height)

    def update(self, *args, **kwargs):
        """updates values to attributes using *args"""
        if len(args) > 0:
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.__width = j
                if i == 2:
                    self.__height = j
                if i == 3:
                    self.__x = j
                if i == 4:
                    self.__y = j
        elif len(kwargs) > 0:
            for x, y in kwargs.items():
                if x == 'id':
                    self.id = y
                if x == 'width':
                    self.__width = y
                if x == 'height':
                    self.__height = y
                if x == 'x':
                    self.__x = y
                if x == 'y':
                    self.__y = y

    def to_dictionary(self):
        """prints the dictionary representation of rectangle"""
        obj = {}
        for i in ['id', 'width', 'height', 'x', 'y']:
            obj[i] = getattr(self, i)
        return obj
