#!/usr/bin/python3
"""
Module: 8-class_to_json
Contains function to convert class object to JSON-serializable dictionary
"""


def class_to_json(obj):
    """
    Returns dictionary description for JSON
    serialization of an object

    Args:
        obj: Instance of a Class

        Returns:
        dict: Dictionary with all serializable attributes
    """
    result = {}

    for attr_name in dir(obj):
        if not attr_name.startswith('__'):
            attr_value = getattr(obj, attr_name)
            if isinstance(attr_value, (dict, list, str, int, bool)):
                result[attr_name] = attr_value

    return result
