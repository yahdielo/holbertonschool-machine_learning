#!/usr/bin/env python3

"""
    This module adds the elements of two arrays and returns a new array,
    or rather adds tho vectors together suming each element of arr1 with each
    element of arra2
"""


def add_arrays(arr1, arr2):

    """
        This module adds the elements of two arrays and returns a new array,
        or rather adds tho vectors together suming each element
         of arr1 with each element of arra2
    """
    newArray = []
    if len(arr1) == len(arr2):
        newArray = [arr1[i] + arr2[i] for i in range(len(arr1))]

        return newArray

    return None
