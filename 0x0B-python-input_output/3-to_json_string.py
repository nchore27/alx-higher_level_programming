#!/usr/bin/python3
"""defines a function to_json_string"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object
    Args:
        my_obj: object
    """
    return json.dumps(my_obj, sort_keys=True)
