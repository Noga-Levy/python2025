"""
Written on February 2, 2025, by Noga Levy.

This program finds all the integer factors, both negative and positive, of any number.
"""

import math


def find_factors(n):

    if n == 0:
        return "all numbers (0 has infinite factors)"

    num = abs(n)
    pos_factors = {j for i in range(1, math.ceil(math.isqrt(num)) + 1) if num % i == 0 for j in (i, num//i)}
    factors_grouped = sorted([-k for k in pos_factors]) + sorted([k for k in pos_factors])

    return (", ".join(str(factors_grouped[c]) for c in range(len(factors_grouped) - 2)) + " and " +
            str(factors_grouped[-1]))


numToFactor = input("Which number do you want the factors of? Enter here: ")

while not numToFactor.lstrip('-').isdigit():
    numToFactor = input("Please write a integer, not a character or fraction: ")

print(f"The factors of {numToFactor} are {find_factors(int(numToFactor))}.")
