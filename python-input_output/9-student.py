#!/usr/bin/python3
"""
Module: 9-student
Defines a Student class with JSON serialization capability
"""


class Student:
    """
    Student class representing a student

    Attributes:
        first_name (str): Student's first name
        last_name (str): Student's last name
        age (int): Student's age
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student instance

        Args:
            first_name (str): First name of the student
            last_name (str): Last name of the student
            age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):

        """
        Retrieve a dictionary representation of a Student instance

        Returns:
            dict: Dictionary containing student attributes
        """
        result = {}

        for attr_name in dir(self):
            if not attr_name.startswith('__'):
                attr_value = getattr(self, attr_name)

                if isinstance(attr_value, (dict, list, str, int, bool)):
                        result[attr_name] = attr_value

                        return result
