"""
Written in March 2025 by Noga Levy.

This program finds all the common factors for any number of numbers. The user defines how many numbers to find the
common factor of, and afterward, defines what those numbers are.
"""


import math


def all_factors(n):

    if n == 0:
        return "all numbers (0 has infinite factors)"

    num = abs(n)
    pos_factors = {j for i in range(1, math.ceil(math.isqrt(num)) + 1) if num % i == 0 for j in (i, num//i)}
    factors_grouped = [-k for k in pos_factors] + [k for k in pos_factors]

    return factors_grouped


numberOfComparingNums = input("How many numbers are we comparing? ")

while not numberOfComparingNums.isdigit():
    numberOfComparingNums = input("Please write a positive integer, not a character, fraction, or negative number: ")

comparingNumList = []

for number in range(int(numberOfComparingNums)):
    add = input(f"Enter number {number + 1}: ")

    while not add.lstrip('-').isdigit():
        add = input("Please write a integer, not a character or fraction: ")

    comparingNumList.append(int(add))

factors = set(all_factors(comparingNumList[0]))
remove_factor = []

"""
for amountComparing in range(1, int(numberOfComparingNums)):
    for factor in range(len(factors)):
        if factors[factor] not in all_factors(comparingNumList[amountComparing]):
            remove_factor.append(factors[factor])
"""

for amountComparing in comparingNumList[1:]:
    factors.intersection_update(all_factors(amountComparing))

factors = sorted(set(f for f in factors if f not in remove_factor))
print(f"The common factors of the numbers listed are: {factors}")
