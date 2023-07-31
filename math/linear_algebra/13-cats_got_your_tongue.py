#!/usr/bin/env python3

"""concatenates two matrices along a specific axis:"""


import numpy as np



def np_cat(mat1, mat2, axis=0):
    """ concatenates two matrices along a specific axis: using
        np.concat and returning a new nparray
    """
    return np.concatenate((mat1, mat2), axis=axis)
