#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list

    Args:
        my_list: List of integers

    Returns:
        New list with True/False for each element divisible by 2
    """
    result = []
    for num in my_list:
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)
    return result
