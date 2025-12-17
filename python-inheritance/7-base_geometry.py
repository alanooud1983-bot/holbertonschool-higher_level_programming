#!/usr/bin/python3
"""
Module: 7-base_geometry
Contains class BaseGeometry with area() and integer_validator() methods
"""


class BaseGeometry:
    """
    Base geometry class with validation methods.
    
    This class serves as a base for other geometry classes.
    """
    
    def area(self):
        """
        Calculate the area of the geometry.
        Raises:
            Exception: Always raises with message
            "area() is not implemented"
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        Args:
            name (str): The name of the parameter
            (used in error messages)
            value: The value to validate
            Raises:
            TypeError: If value is not an integer
            ValueError: If value is less than or equal to 0
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
