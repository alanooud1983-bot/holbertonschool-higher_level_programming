#!/usr/bin/python3
"""
Module: 2-matrix_divided
Function to divide all elements of a matrix by a number
"""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number

    Args:
        matrix (list of lists): Matrix of integers or floats
        div (int or float): Number to divide by

    Returns:
        list of lists: New matrix with divided elements

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
        TypeError: If rows are not the same size
        TypeError: If div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
            )

    if len(matrix) == 0 or all(len(row) == 0 for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of integers/floats"
                )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for element in row:
            result = element / div

            result_str = f"{result:.10f}"

            if '.' in result_str:
                int_part, dec_part = result_str.split('.')
                dec_3_digits = dec_part[:3].ljust(3, '0')

                int_val = int(int_part) if int_part else 0
                dec_val = int(dec_3_digits[:2])
                third_digit = int(dec_3_digits[2]) if len(dec_3_digits) > 2 else 0

                if third_digit >= 5:
                    dec_val += 1
                    if dec_val >= 100:
                        int_val += 1
                        dec_val = 0

                rounded = int_val + (dec_val / 100.0)

                if result < 0 and rounded == 0:
                    rounded = -0.0

                new_row.append(rounded)
            else:
                new_row.append(float(result_str))

        new_matrix.append(new_row)

    return new_matrix
