#!/usr/bin/python3
"""
Module: 0-lookup
Contains function: lookup
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object. 
    Args:
        obj: Any Python object 
    Returns:
        list: A list of strings containing the names of attributes and methods
    """
    return dir(obj)
