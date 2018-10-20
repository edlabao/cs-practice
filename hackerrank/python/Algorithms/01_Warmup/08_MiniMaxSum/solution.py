#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/mini-max-sum/problem
Level: Easy
Score: 10

Example:
1 2 3 4 5
> 10 14
"""


def solve(ar):
    """
    Given an array of 5 integers, return the minimal and maximal sum of 4 out of
    5 of the integers.
    """
    # Just sort the list of integers in place and take the sum of the first 4
    # then the last 4.
    ar.sort()
    minSum = reduce((lambda x, y: x + y), ar[0:4])
    maxSum = reduce((lambda x, y: x + y), ar[1:5])
    return (minSum, maxSum)


if __name__ == "__main__":

    # Problem input/output.
    ar = map(int, raw_input().strip().split(' '))
    print "%d %d" % solve(ar)
