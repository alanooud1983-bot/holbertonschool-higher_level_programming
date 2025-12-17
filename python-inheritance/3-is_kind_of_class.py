#!/usr/bin/python3
"""
Module: 3-is_kind_of_class
Contains function: is_kind_of_class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or inherited from,
    the specified class.
    Args:
        obj: Any Python object
        a_class: A class to check against
    Returns:
        bool: True if obj is an instance of a_class or its subclass,
        False otherwise
    """
    return isinstance(obj, a_class)
