#!/usr/bin/python3
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
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return a + b
