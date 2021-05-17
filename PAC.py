"""
PAC(Permutations and Combinations)
This file contains functions related to permutations and combinations.
"""

def factorial(num):
    if num > 1:
        return num * factorial(num - 1)
    else:
        return 1

# permutation functions
def permutation(n, r):
    return factorial(n) / factorial(n - r)
    
def productPermutation(n, r):
    return n ** r

def pupilPermutation(n, *pupil):
    denominator = 1
    for sequence in pupil:
        denominator *= factorial(sequence)

    return factorial(n) / denominator

# combination functions
def combination(n, r):
    if r == 0:
        return 1
    else:
        return factorial(n) / (factorial(r) * factorial(n - r))

def homogeneousProduct(n, r):
    return combination(n + r - 1, r)

def binomialTheorem(a, b, n, general : int = None):
    if general is not None:
        coefficient = []

        coefficient.append(combination(n, general - 1))
        coefficient.append(combination(n, general - 1) * (a ** (n - general + 1)) * (b ** (general - 1)))

        return coefficient
    else:
        value = 0
        for sequence in range(n+1):
            value += combination(n - sequence, sequence) * (a ** (n - sequence)) * (b ** sequence)

        return value