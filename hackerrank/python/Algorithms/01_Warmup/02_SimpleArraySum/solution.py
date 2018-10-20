#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/simple-array-sum/problem
Level: Easy
Score: 10

Example:
6
1 2 3 4 10 11
> 31
"""


def solve(n, ar):
    """
    Given an integer array of size n, return the sum of all its elements.
    """
    # We could explicitly iterate over each element the array, but in python,
    # we can just use the reduce() function to sum up a list of numbers.
    return reduce((lambda x, y: x + y), ar)


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    print solve(n, ar)
