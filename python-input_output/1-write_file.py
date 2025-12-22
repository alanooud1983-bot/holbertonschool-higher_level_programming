#!/usr/bin/python3
"""
Module: 1-write_file
Contains function: write_file
"""


def write_file(filename="", text=""):
    """
    Writes a string to a text file
    and returns the number of characters written.

    Args:
        filename (str): The name of the file to write to.
        Defaults to empty string.
        text (str): The text to write to the file.
        Defaults to empty string.

        Returns:
        int: Number of characters written to the file.
    """
    with open(filename, 'w', encoding='utf-8') as file:
        chars_written = file.write(text)
        return chars_written
