"""Code that will solve first derivative of a polynomial problems"""
import numpy as np
import matplotlib.pyplot as plt

def poly_derivative(poly):
    """Function that calculates the derivative of a polynomial"""
    if type(poly) != list or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    if type(poly[0]) != int and type(poly[0]) != float:
        return None
    for i in range(1, len(poly)):
        if type(poly[i]) != int and type(poly[i]) != float:
            return None
    derivative = []
    for i in range(1, len(poly)):
        derivative.append(i * poly[i])
    return derivative

poly = [9, 5, 35, 90, 64]

print(poly_derivative(poly))