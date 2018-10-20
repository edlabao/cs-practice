#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/diagonal-difference/problem
Level: Easy
Score: 10

Example:
3
11 2 4
4 5 6
10 8 -12
> 15
"""


def solve(n, ar):
    """
    Return the absolute sum of the nxn matrix defined by ar.
    """
    # Initialize the sum of the diagonals 1 and 2.
    d1sum = 0
    d2sum = 0

    # Iterate through the list of n-sized lists, one row at a time and use
    # enumerate() to generate the current index value which we'll use to
    # determine the indeces of each diagonal to use later.
    for (ridx, row) in enumerate(ar):
        # Add the appropriate value to the diagonal sums starting on opposite
        # ends of the row and moving inward based on the current row index.
        d1sum += row[ridx]
        d2sum += row[n - ridx - 1]

    # Return the absolute value of the difference of the diagonal sums.
    return abs(d1sum - d2sum)


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int, raw_input().strip().split(' '))
        a.append(a_temp)
    print solve(n, a)
