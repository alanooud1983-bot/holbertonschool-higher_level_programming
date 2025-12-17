#!/usr/bin/python3
"""
Module: 2-is_same_class
Contains function: is_same_class
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class
    Args:
        obj: Any Python object
        a_class: A class to check against
        Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise
    """
    return type(obj) is a_class
