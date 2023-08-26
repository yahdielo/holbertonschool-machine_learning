#!/usr/bin/env python3

""" class Neuron that defines a single neuron
    performing binary classification
"""

import numpy as np


class Neuron:
    """
        class Neuron that defines a single neuron
        performing binary classification
    """
    def __init__(self, nx):

        if type(nx) != int:
            raise TypeError("nx must be an integer")

        if nx < 1:
            raise ValueError("nx must be a positive integer")

        self.__b = 0
        self.__W = np.random.normal(size=(1, nx))
        self.__A = 0

    @property
    def W(self):
        return self.__W

    @property
    def b(self):
        return self.__b

    @property
    def A(self):
        return self.__A
