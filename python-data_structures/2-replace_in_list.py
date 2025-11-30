#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """
    Replace an element in a list at specific position

    Args:
        my_list: The list
        idx: Index to replace
        element: New element to insert

    Returns:
        Modified list or original list if index invalid
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list
