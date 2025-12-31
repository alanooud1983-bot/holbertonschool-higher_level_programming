#!/usr/bin/python3
"""Module that provides a function to add two integers."""


def add_integer(a, b=98):
    """Add two integers or floats and return an integer result."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast floats to int safely (handles float overflow cases)
    try:
        a = int(a)
    except (OverflowError, ValueError):
        # Keep OverflowError behavior for huge floats (inf) or invalid numeric floats
        raise
    try:
        b = int(b)
    except (OverflowError, ValueError):
        raise

    return a + b
