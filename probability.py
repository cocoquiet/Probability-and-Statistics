"""
This file contains the function of probability.
"""

from PAC import combination

def probability(A, S):
    return A / S

def conditionalProbability(intersection, A):
    return intersection / A

def independentEnforcement(n, r, p):
    return combination(n, r) * (1 - p) ** (n - r)