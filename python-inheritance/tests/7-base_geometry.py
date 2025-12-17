#!/usr/bin/python3
"""
Module: 7-base_geometry
Contains class BaseGeometry with area() and integer_validator() method
"""


class BaseGeometry:
    """
    Base geometry class with validation methods.
    """
    
    def area(self):
        """
        Calculate the area of the geometry.
        """
        raise Exception("area() is not implemented")
    
    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
