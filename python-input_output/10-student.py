#!/usr/bin/python3
"""
Module: 10-student
Defines a Student class with filtered JSON serialization
"""


class Student:
    """
    Student class representing a student with filtered JSON output

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

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance

        Args:
            attrs (list): Optional list of attribute names to include

        Returns:
            dict: Dictionary containing specified student attributes
        """
        if attrs is None:
            return self._get_all_attributes()

        result = {}
        for attr_name in attrs:
            if isinstance(attr_name, str):
                if hasattr(self, attr_name):
                    attr_value = getattr(self, attr_name)
                    if isinstance(attr_value, (dict, list, str, int, bool)):
                        result[attr_name] = attr_value

        return result

    def _get_all_attributes(self):
        """
        Helper method to get all serializable attributes

        Returns:
            dict: All serializable attributes
        """
        result = {}
        for attr_name in dir(self):
            if not attr_name.startswith('__'):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (dict, list, str, int, bool)):
                    result[attr_name] = attr_value
        return result
