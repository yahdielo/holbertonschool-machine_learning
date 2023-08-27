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

    def cost(self, Y, A):
        """ Calculates the cost of the model using logistic regression
            Y: is a numpy.ndarray with shape (1, m) that contains
            the correct labels for the input data.
            A: is a numpy.ndarray with shape (1, m) containing
            the activated output of the neuron for each example
            Returns the cost
        """
        m = Y.shape[1]  # Number of examples

        # Avoid division by zero errors by using a small value
        epsilon = 1e-7

        # Calculate the cost using the logistic regression formula
        cost = ((-1 / m) * np.sum(Y * np.log(A + epsilon)
                + (1 - Y) * np.log(1 - A + epsilon)))

        return cost
