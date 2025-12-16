#!/usr/bin/python3
"""
Module: 1-my_list
Contains class: MyList that inherits from list
"""


class MyList(list):
    """
    A custom list class that inherits from the built-in list class.
    
    This class adds a method to print the list in sorted order
    without modifying the original list.
    """
    
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        
        This method creates a sorted copy of the list and prints it.
        The original list remains unchanged.
        
        Returns:
            None
        """
        # Create a sorted copy of the list and print it
        sorted_list = sorted(self)
        print(sorted_list)
