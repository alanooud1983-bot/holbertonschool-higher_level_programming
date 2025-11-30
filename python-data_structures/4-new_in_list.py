#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace element in a copy of list without modifying original

    Args:
        my_list: The original list
        idx: Index to replace
        element: New element to insert

    Returns:
        New list with replacement or copy of original if index invalid
    """
    new_list = my_list.copy()

    if idx < 0 or idx >= len(new_list):
        return new_list

    new_list[idx] = element
    return new_list
