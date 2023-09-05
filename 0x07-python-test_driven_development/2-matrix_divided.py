#!/usr/bin/python3
"""A function that divides a matrix."""


def matrix_divided(matrix, div):
    """
    matrix_divided: a function that divides a matrix.

    Args:
    matrix: a matrix that the division operation will be performed upon.
    div: a divisor.

    """
    # Check if matrix is a list of lists
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) "
                        "of integers/floats")

    # Check if all rows have the same size
    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) > 1:
        raise TypeError("Each row of the matrix must have the same size")

    # Check if div is a number
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    # Check if div is not zero
    if div == 0:
        raise ZeroDivisionError("division by zero")

    # Divide each element of the matrix and create a new matrix
    divided_matrix = []
    for row in matrix:
        divided_row = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) "
                                "of integers/floats")
            divided_element = round(element / div, 2)
            divided_row.append(divided_element)
        divided_matrix.append(divided_row)

    return divided_matrix
