#!/usr/bin/env python3

class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = sum(data) / len(data)
    
    def pmf(self, k):
        if not isinstance(k, int):
            k = int(k)
        
        if k < 0:
            return 0
        
        e_to_the_power = 2.71828 ** -self.lambtha
        k_factorial = 1
        for i in range(1, k + 1):
            k_factorial *= i
        
        pmf_value = (self.lambtha ** k) * e_to_the_power / k_factorial
        return pmf_value
