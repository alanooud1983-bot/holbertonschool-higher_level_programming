#!/usr/bin/python3
"""
Module: 3-say_my_name
Function to print "My name is <first_name> <last_name>"
"""


def say_my_name(first_name, last_name=""):
    """
    Print "My name is <first_name> <last_name>"
    
    Args:
        first_name (str): First name
        last_name (str, optional): Last name. Defaults to "".
        
    Raises:
        TypeError: If first_name is not a string
        TypeError: If last_name is not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    print(f"My name is {first_name} {last_name}")
