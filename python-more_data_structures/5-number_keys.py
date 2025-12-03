#!/usr/bin/python3
def number_keys(a_dictionary):
    """
    Count the number of keys in a dictionary
    Args:
        a_dictionary: The dictionary
    Returns:
        Number of keys in the dictionary
    """
    count = 0
    for key in a_dictionary:
        count += 1
    return count
