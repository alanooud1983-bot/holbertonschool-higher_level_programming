#!/usr/bin/python3
"""
Module: 6-base_geometry
Contains class BaseGeometry with area() method
"""


class BaseGeometry:
    """
    Base geometry class with area method.
    This class serves as a base for other geometry classes.
    The area() method raises an Exception since it should be
    implemented by subclasses.
    """
    def area(self):
        """
        Calculate the area of the geometry.
        
        Raises:
        Exception: Always raises with message
        "area() is not implemented"
            Note:
            This method should be overridden by subclasses.
        """
        raise Exception("area() is not implemented")
