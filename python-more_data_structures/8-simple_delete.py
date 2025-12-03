#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """
    Delete a key from dictionary
    Args:
        a_dictionary: Dictionary to modify
        key: Key to delete
    Returns:
        Modified dictionary
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
