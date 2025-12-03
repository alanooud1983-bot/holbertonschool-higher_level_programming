#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurrences of an element in a list
    Args:
        my_list: The initial list
        search: Element to replace
        replace: New element
    Returns:
        New list with replaced elements
    """
    new_list = []
    for item in my_list:
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list
