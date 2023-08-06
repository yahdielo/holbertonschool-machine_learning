#!/usr/bin/env python3

""" This module multiplies two matrixes returning a new matrix """


def mat_mul(mat1, mat2):
        """     This module multiplies  creating a new one, 
                with the size of the outter dimensions
                of matrixA and matrixB. Then we creat a nested loop
                to iterate in side the newMatrix, and with list comprehenssion
                as we itirated in newMatrix we create another loop
                to multiply the 2 matrices and assing a the value of the multiplication
        """
        if len(mat1[0]) != len(mat2):
                return None

        newMatrix = [[0 for _ in range(len(mat2[0]))]
                        for _ in range(len(mat1))]

        for i in range(len(newMatrix)):
                for j in range(len(newMatrix[0])):
                        newMatrix[i][j] = sum(mat1[i][k] * mat2[k][j] 
                                              for k in range(len(mat1[0])))

        return newMatrix
