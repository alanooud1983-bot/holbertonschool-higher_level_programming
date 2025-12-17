#!/usr/bin/python3
"""
Module: 4-inherits_from
Contains function: inherits_from
"""


def inherits_from(obj, a_class):
    """
    Checks if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj: Any Python object
        a_class: A class to check against
        Returns:
        bool: True if obj is an instance of a subclass of a_class,
              False otherwise
    """
    return type(obj) is not a_class and isinstance(obj, a_class)
