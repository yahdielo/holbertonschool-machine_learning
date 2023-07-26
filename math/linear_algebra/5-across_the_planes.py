#!/usr/bin/env python3

""" This modules sums two matrixes together"""


def add_matrices2D(mat1, mat2):
    """ This modules sums two matrixes together """

    M1Shape = (len(mat1), len(mat1[0]))
    M2Shape = (len(mat2), len(mat2[0]))

    if M1Shape == M2Shape:
        newMatrix = [[mat1[i][j] + mat2[i][j] for i in range(len(mat1))]
                     for j in range(len(mat1[0]))]
        return newMatrix

    return None
