#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """
    Print dictionary with keys sorted alphabetically
    Args:
        a_dictionary: Dictionary to print
    """
    for key in sorted(a_dictionary.keys()):
        print("{}: {}".format(key, a_dictionary[key]))
