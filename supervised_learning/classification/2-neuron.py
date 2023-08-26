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
        """ This getter, returns all the weight values """
        return self.__W

    @property
    def b(self):
        """ This getter returns the value of the Bias """
        return self.__b

    @property
    def A(self):
        """ This getter returns the activation value """
        return self.__A

    def forward_prop(self, X):
        """ This function perfomrs froward propagation"""
        z = np.dot(self.__W, X) + self.__b

        self.__A = 1 / (1 + np.exp(-z))

        return self.__A
