#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/plus-minus/problem
Level: Easy
Score: 10

Example:
6
-4 3 -9 0 4 1
> 0.500000
> 0.333333
> 0.166667
"""


def solve(n, ar):
    """
    Given an integer array ar of size n, return the decimal fraction of the
    number of positive numbers, negative numbers and zeroes. Test cases are
    scaled to 6 decimal places.
    """

    num_pos = 0
    num_neg = 0
    num_zero = 0

    for i in ar:
        if i > 0:
            num_pos += 1
        elif i < 0:
            num_neg += 1
        else:
            num_zero += 1

    # Return the ratios but cast to float to ensure preservation of precision.
    return (float(num_pos) / float(n),
            float(num_neg) / float(n),
            float(num_zero) / float(n))


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))

    (pos, neg, zero) = solve(n, arr)

    # Print the answers to 6 decimal places. We handle the precision in the output
    # since the problem requirements didn't require being able to do anything with
    # the values other than printing them. Otherwise we would probably use the
    # Decimal library to ensure values are at the right precision.
    print "{:0.6f}".format(pos)
    print "{:0.6f}".format(neg)
    print "{:0.6f}".format(zero)
