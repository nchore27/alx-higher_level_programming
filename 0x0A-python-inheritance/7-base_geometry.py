#!/usr/bin/python3
"""defines a class
"""


class BaseGeometry:
    """presents base geometry
    """
    def area(self):
        """raise exception if not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Raise errors when value is not int or is <= 0
        Args:
            name: name
            value: value
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
