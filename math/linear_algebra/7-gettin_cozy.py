#!/usr/bin/env python3

""" This functions concatenates two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ This functions concatenates two matrices"""

    if axis == 0 and len(mat1[0]) != len(mat2[0]):
        return None
    if axis == 1 and len(mat1) != len(mat2):
        return None

    newmatrix = []
    if axis == 0:
        newmatrix = mat1 + mat2
        newmatrix = newmatrix.copy()
        return newmatrix
    else:
        for i in range(len(mat1)):
            newmatrix.append(mat1[i] + mat2[i])
        return newmatrix
    