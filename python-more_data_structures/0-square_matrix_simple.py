#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Compute square of all integers in a matrix
    Args:
        matrix: 2D list of integers
    Returns:
        New matrix with squared values
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return new_matrix
