#!/usr/bin/python3
"""
Module: 0-read_file
Contains function: read_file
"""


def read_file(filename=""):
    """
    Reads a text file (UTF8) and prints its content to stdout.

    Args:
        filename (str): The name of the file to read.
        Defaults to empty string.

        Returns:
        None
    """
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content, end='')
