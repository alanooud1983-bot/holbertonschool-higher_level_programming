#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Delete item at specific position in a list

    Args:
        my_list: The list to modify
        idx: Index of item to delete

    Returns:
        Modified list or original list if index invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list
