#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieve an element from a list at specific index    
    
    Args:
        my_list: The list
        idx: The index to retrieve
    Returns:
        Element at index or None if index is invalid
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
