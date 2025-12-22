#!/usr/bin/python3
"""
Module: 4-from_json_string
Contains function: from_json_string
"""

import json


def from_json_string(my_str):
    """
    Returns an object (Python data structure)
    represented by a JSON string.

    Args:
        my_str (str): The JSON string to convert to Python object

        Returns:
        object: Python data structure (dict, list, etc.)
        from JSON string
    """
    return json.loads(my_str)
