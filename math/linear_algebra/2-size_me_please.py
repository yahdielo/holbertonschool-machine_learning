#!/usr/bin/env python3
"""
    This module calculates the shape of a matrix,
    calculating the rowns, columns and matrixes.
    The formula use to calculate rows is len(matrix),
    and to get the columns is len(matrix[0])
"""
def matrix_shape(matrix):
    """
        This module calculates the shape of a matrix,
        calculating the rowns, columns and matrixes.
        The formula use to calculate rows is len(matrix),
        and to get the columns is len(matrix[0])
    """
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0] 
    return shape