#!/usr/bin/python3
def no_c(my_string):
    """
    Remove all characters 'c' and 'C' from a string

    Args:
        my_string: The input string

    Returns:
        New string without 'c' or 'C' characters
    """
    new_string = ""
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
