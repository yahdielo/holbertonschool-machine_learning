#!/usr/bin/env python3

""" This modules transverse a 2D matrix """


def matrix_transpose(matrix):
    """ This modules transverse a 2D matrix """
    temp = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp[j][i] = matrix[i][j]
            
    return temp
                



print(matrix_transpose(matrix))
            
                
                

