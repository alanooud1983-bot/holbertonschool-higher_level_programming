#!/usr/bin/python3
"""
Module: 2-append_write
Contains function: append_write
"""


def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file
    and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to.
        Defaults to empty string.
        text (str): The text to append to the file.
        Defaults to empty string.

        Returns:
        int: Number of characters added to the file.
    """
    with open(filename, 'a', encoding='utf-8') as file:
        chars_added = file.write(text)
        return chars_added
