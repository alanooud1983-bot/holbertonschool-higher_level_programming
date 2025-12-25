#!/usr/bin/python3
"""
Module: task_00_basic_serialization
Basic serialization module for JSON operations
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary and save it to a JSON file
    
    Args:
        data (dict): Python dictionary to serialize
        filename (str): Name of the output JSON file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)
    
    print(f"Data serialized and saved to '{filename}'")


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it to a Python dictionary
    
    Args:
        filename (str): Name of the input JSON file
        
    Returns:
        dict: Python dictionary with the deserialized data
    """
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    print(f"Data loaded and deserialized from '{filename}'")
    return data
