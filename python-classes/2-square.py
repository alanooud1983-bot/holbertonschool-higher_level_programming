#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Defines a square with size validation"""

    def _init_(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
