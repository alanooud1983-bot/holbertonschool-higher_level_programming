#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Update or add key/value in a dictionary
    Args:
        a_dictionary: Dictionary to update
        key: Key to update/add
        value: Value to set
    Returns:
        Updated dictionary
    """
    a_dictionary[key] = value
    return a_dictionary
