"""
1. First, pick a number.

2. Then, add 38 to your number

3. Third, divide your new number by 2

4. Multiply what you got by 51

5. Divide by 17

6. Multiply by 4/3

7. Subtract two times your original number

8. Did you get 76? Answer: yes.
"""

"""
Proof: The equation simplifies to 76, as the number chosen is cancelled in the last step.

( ( ( (38 + n)/2 ) * 51) / 17) * 4/3) - 2n =
                                           => (((38 + n)/2) * 3 * 4/3) - 2n
                                           => (((38 + n)/2) * 4) - 2n
                                           => 2(38 + n) - 2n
                                           => 2(38)
                                           => 76.

"""

for originalNum in range(12):
    nextNumInSeries = originalNum + 38
    print(nextNumInSeries)

    nextNumInSeries = nextNumInSeries / 2
    print(nextNumInSeries)

    nextNumInSeries = nextNumInSeries * 51
    print(nextNumInSeries)

    nextNumInSeries = nextNumInSeries / 17
    print(nextNumInSeries)

    nextNumInSeries = nextNumInSeries * 4/3

    nextNumInSeries = nextNumInSeries - (2 * originalNum)
    print(f"{nextNumInSeries} \n\n\n")