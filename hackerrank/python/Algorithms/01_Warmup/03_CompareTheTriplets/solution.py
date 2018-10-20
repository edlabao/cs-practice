#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/compare-the-triplets/problem
Level: Easy
Score: 10

Example:
5 6 7
3 6 10
> 1 1
"""


def solve(a0, a1, a2, b0, b1, b2):
    """
    Given two triplets A(a0, a1, a2) and B(b0, b1, b2) calculate the comparison
    points of each triplet with the following rules:
        If a[i] > b[i], then A gets 1 point
        If a[i] < b[i], then B gets 1 point
        If a[i] == b[i], then no points are awarded
    """
    # Initialize the comparison sums of each triplet.
    asum = 0
    bsum = 0

    # Repackage the triplets into tuples containing the elements to compare to
    # make it easier.
    for (a, b) in ((a0, b0), (a1, b1), (a2, b2)):
        if a > b:
            asum += 1
        elif a < b:
            bsum += 1

    return (asum, bsum)


if __name__ == "__main__":

    # Problem input/output.
    a0, a1, a2 = raw_input().strip().split(' ')
    a0, a1, a2 = [int(a0), int(a1), int(a2)]
    b0, b1, b2 = raw_input().strip().split(' ')
    b0, b1, b2 = [int(b0), int(b1), int(b2)]

    result = solve(a0, a1, a2, b0, b1, b2)
    print " ".join(map(str, result))
