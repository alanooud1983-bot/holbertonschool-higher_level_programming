#!/usr/bin/python3
"""
Module: task_01_pickle
Custom object serialization using pickle module
"""

import pickle


class CustomObject:
    """
    A custom Python class with serialization capabilities using pickle

    Attributes:
        name (str): The name of the person
        age (int): The age of the person
        is_student (bool): Whether the person is a student
    """

    def __init__(self, name, age, is_student):
        """
        Initialize a new CustomObject instance

        Args:
            name (str): The name
            age (int): The age
            is_student (bool): Student status
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        Display the object's attributes in the specified format
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the object and save it to a file using pickle

        Args:
            filename (str): The name of the file to save to

        Returns:
            bool: True if serialization succeeded, False otherwise
        """
        try:
            if not isinstance(filename, str):
                print("Error: Filename must be a string")
                return False

            with open(filename, 'wb') as f:
                pickle.dump(self, f)

            print(f"Object successfully serialized to '{filename}'")
            return True

        except (pickle.PicklingError, TypeError) as e:
            print(f"Error: Could not serialize object - {e}")
            return False
        except PermissionError:
            print(f"Error: Permission denied for file '{filename}'")
            return False
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")
            return False

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from a file using pickle

        Args:
            filename (str): The name of the file to load from

        Returns:
            CustomObject or None: The deserialized object, or None if failed
        """
        try:
            if not isinstance(filename, str):
                print("Error: Filename must be a string")
                return None

            with open(filename, 'rb') as f:
                obj = pickle.load(f)

            if not isinstance(obj, cls):
                print(f"Error: Loaded object is not of type {cls.__name__}")
                return None

            print(f"Object successfully deserialized from '{filename}'")
            return obj

        except FileNotFoundError:
            print(f"Error: File '{filename}' not found")
            return None
        except pickle.UnpicklingError:
            print(f"Error: File '{filename}' is not a valid pickle file")
            return None
        except PermissionError:
            print(f"Error: Permission denied for file '{filename}'")
            return None
        except EOFError:
            print(f"Error: File '{filename}' is empty or corrupted")
            return None
        except Exception as e:
            print(f"Error: An unexpected error occurred - {e}")
            return None
