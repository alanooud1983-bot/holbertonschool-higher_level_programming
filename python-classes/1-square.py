#!/usr/bin/python3
"""Square class with private size"""

class Square:
    """Square class with private instance attribute size"""
    def __init__(self, size):
        """Initialize square with size
        Args:
            size: size of the square"""
        self.__size = size
