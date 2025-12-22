#!/usr/bin/python3
"""
Module: 11-student
Defines a Student class with JSON serialization/deserialization
"""


class Student:
    """
    Student class with JSON serialization and deserialization capabilities

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
        all_attrs = {}
        for attr_name in dir(self):
            if not attr_name.startswith('__'):
                attr_value = getattr(self, attr_name)
                if isinstance(attr_value, (dict, list, str, int, bool)):
                    all_attrs[attr_name] = attr_value

        if attrs is None:
            return all_attrs

        if not isinstance(attrs, list):
            return all_attrs

        filtered = {}
        for attr_name in attrs:
            if isinstance(attr_name, str) and attr_name in all_attrs:
                filtered[attr_name] = all_attrs[attr_name]

        return filtered

    def reload_from_json(self, json):
        """
        Replace all attributes of the Student instance from a dictionary

        Args:
            json (dict): Dictionary containing attribute names and values
        """
        if not isinstance(json, dict):
            return

        for key, value in json.items():
            if isinstance(key, str):
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    setattr(self, key, value)
