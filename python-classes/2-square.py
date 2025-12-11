#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Defines a square with size validation"""
    
    def __init__(self, size=0):
        """Initialize Square with size validation"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
