#!/usr/bin/env python3

""" this modules concatenates thwo arrays"""


def cat_arrays(arr1, arr2):

    """ this modules concatenates thwo arrays"""

    if arr1 and arr2:
        newList = []
        newList.append(list(arr1) + list(arr2))
        return newList
    return None
