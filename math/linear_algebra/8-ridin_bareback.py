#!/usr/bin/env python3

""" This module multiplies two matrixes returning a new matrix """


def mat_mul(mat1, mat2):
        """
                This function performs multiplication of two given matrixes
        """

        if len(mat1[0]) != len(mat2):
                return None

        newMatrix = [[0 for _ in range(len(mat2[0]))]
                        for _ in range(len(mat1))]

        for i in range(len(newMatrix)):
                for j in range(len(newMatrix[0])):
                        newMatrix[i][j] = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0])))

        return newMatrix
