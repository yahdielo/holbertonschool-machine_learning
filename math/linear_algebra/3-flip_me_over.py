#!/usr/bin/env python3

""" This modules transverse a matrix """


def matrix_transpose(matrix):
    """ This modules transverse a 2D matrix
        creating a new matrix with nested list comprehension,
        creating a matrix with the same dimensions and 
        adding the transverse values to the newmatrix
    """

    rows = len(matrix)
    col = len(matrix[0])

    #nested list comprehension
    #declares 0 as is the value will initialize each/
    #// space in this new matrix//
    #for _ as i dont want to run inside the array in range of rows
    #// and a nested loop to run in the columns of the matrix
    newMatrix = [[0 for _ in range(rows)] for _ in range(col)]

    for i in range(rows):
        for j in range(col):
            newMatrix[j][i] = matrix[i][j]
            
    return newMatrix
