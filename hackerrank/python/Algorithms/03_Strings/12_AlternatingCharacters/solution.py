#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/alternating-characters/problem
Level: Easy
Score: 20
"""


def solve(s):
    """
    Function that accepts a string, s, and returns the minimum number of
    deletions required to ensure that every two consecutive characters are
    different.
    """

    # Initialize the answer which is the number of deletions required.
    answer = 0

    # Keep track of the previous character we saw.
    prev = None

    # Iterate thru the string and look for identical consecutive characters.
    # Each time we see consecutive characters, increment our counter.
    for c in s:
        if c == prev:
            answer += 1
        prev = c

    return answer


if __name__ == "__main__":

    # Problem input/output.
    q = int(raw_input().strip())
    for a0 in xrange(q):
        s = raw_input().strip()
        result = solve(s)
        print(result)
