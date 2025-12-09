#!/usr/bin/python3
"""
Function that adds 2 integers.
"""


def add_integer(a, b=98):
    """Adds two integers or floats after casting.

    Args:
        a: first number
        b: second number

    Returns:
        int: addition of a and b

    Raises:
        TypeError: if a or b are not int or float
        ValueError: if a or b are NaN
    """
    if isinstance(a, float) and (a != a):
        raise ValueError("cannot convert float NaN to integer")
    if isinstance(b, float) and (b != b):
        raise ValueError("cannot convert float NaN to integer")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
