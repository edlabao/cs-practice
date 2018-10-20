#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/staircase/problem
Level: Easy
Score: 10

Example:
6
>      #
>     ##
>    ###
>   ####
>  #####
> ######
"""


def solve(n):
    """
    Given an integer n, print a staircase n high and n wide at its base and
    ascends to the right.
    """
    results = []
    for i in xrange(n - 1, -1, -1):
        # Use python's character multiplier feature to build the proper string
        # for the current line. The nummber of spaces is the current index (i)
        # and the number of "#" is n minus the number of spaces (i).
        results.append("%s%s" % (" " * i, "#" * (n - i)))
    return results


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())

    for line in solve(n):
        print line
