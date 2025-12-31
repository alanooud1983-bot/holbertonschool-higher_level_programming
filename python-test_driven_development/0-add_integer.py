#!/usr/bin/python3
"""
Module that provides a function to add two integers.
"""


def add_integer(a, b=98):
    """
    Add two integers or floats.

    Args:
        a (int or float): first number
        b (int or float): second number

    Returns:
        int: the addition of a and b
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
