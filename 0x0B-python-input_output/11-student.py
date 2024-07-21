#!/usr/bin/python3
"""Defiens a student class that have to_json public method"""


class Student:
    """a class for a student"""
    def __init__(self, first_name, last_name, age):
        """Initalizes a student object"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns a json representatiion of the object"""
        obj_dict = self.__dict__
        if not attrs:
            return obj_dict
        else:
            alt_dict = {}
            for i in attrs:
                if hasattr(self, i):
                    alt_dict[i] = obj_dict[i]
            return alt_dict

    def reload_from_json(self, json):
        """updates attrs using json file"""
        for i, j in json.items():
            setattr(self, i, j)
