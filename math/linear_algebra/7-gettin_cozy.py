#!/usr/bin/env python3

""" This functions concatenates two matrices"""


def cat_matrices2D(mat1, mat2, axis=0):
    """ This functions concatenates two matrices"""

    newmatrix = []
    if mat1[0] and mat2[0]:
        if axis == 0:
            return mat1 + mat2
        else:
            for i in range(len(mat2)):
                newmatrix.append(mat1[i] + mat2[i])
            return newmatrix
