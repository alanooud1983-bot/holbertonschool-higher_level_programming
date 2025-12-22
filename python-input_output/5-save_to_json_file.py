#!/usr/bin/python3
"""
Module: 5-save_to_json_file
Contains function to save an object to a file using JSON
"""

import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation

    Args:
        my_obj: Python object to serialize
        filename: Name of the file to write to
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
