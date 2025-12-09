#!/usr/bin/python3
"""
Module for adding integers
"""


def add_integer(a, b=98):
    """
    Add two integers
    
    Args:
        a: First number (int or float)
        b: Second number (int or float), default is 98
    
    Returns:
        Integer sum of a and b
    
    Raises:
        TypeError: If a or b is not int or float
    """
    # Check if a is integer or float
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    
    # Check if b is integer or float  
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    # Convert to integers if they are floats
    try:
        a = int(a)
        b = int(b)
    except (ValueError, OverflowError):
        # Handle NaN, infinity, or overflow
        raise TypeError("a must be an integer")
    
    # Perform addition
    return a + b
