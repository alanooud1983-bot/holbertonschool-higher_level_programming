#!/usr/bin/python3
def best_score(a_dictionary):
    """
    Find key with the biggest integer value
    Args:
        a_dictionary: Dictionary with integer values
    Returns:
        Key with maximum value or None if dictionary is empty/None
    """
    if not a_dictionary:
        return None
    max_key = None
    max_value = float('-inf')
    for key, value in a_dictionary.items():
        if value > max_value:
            max_value = value
            max_key = key
    return max_key
