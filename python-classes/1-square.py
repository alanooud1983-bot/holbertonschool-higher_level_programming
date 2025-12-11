#!/usr/bin/python3
"""
Module that defines a Square class with size
"""
class Square:
    """
    A class that defines a square with private size attribute
    Attributes:
        __size (int): The size of the square (private)
    """
    def __init__(self, size):
        """
        Initializes a new Square instance
        Args:
            size (int): The size of the square
        """
        self.__size = size
