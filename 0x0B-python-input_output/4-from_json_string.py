#!/usr/bin/python3
"""defines a function from_json_string"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args:
        my_str: JSON strint
    Return: object
    """
    return json.loads(my_str)
