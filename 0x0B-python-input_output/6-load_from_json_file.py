#!/usr/bin/python3
"""Defines a function load_from_json_file"""
import json


def load_from_json_file(filename):
    """creates an object from a JSON file
    Args:
        filename: JSON file
    """
    with open(filename, 'r', encoding="utf8") as f:
        return json.load(f)
