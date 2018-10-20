#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/a-very-big-sum/problem
Level: Easy
Score: 10

Example:
5
1000000001 1000000002 1000000003 1000000004 1000000005
> 5000000015
"""


def solve(n, ar):
    """
    Return the sum of the elements in array, ar of size n.
    This is the same problem as "Simple Array Sum" but the twist is that the
    elements of the array are in the order of 10^10. In python, however, values
    are autocast to whatever type/size they need to be so we don't actually have
    to change anything.
    """
    # As before, we use the reduce function to calculate the sum.
    return reduce((lambda x, y: x + y), ar)


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    ar = map(long, raw_input().strip().split(' '))
    print solve(n, ar)
