#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/birthday-cake-candles/problem
Level: Easy
Score: 10

Example:
4
3 2 1 3
> 2
"""


def solve(n, ar):

    # Just do a single pass thru the array by keeping track of the maximum
    # height value and the number of times we saw that value.
    max_height = 0
    max_height_count = 0

    for h in ar:
        if h > max_height:
            max_height = h
            max_height_count = 1
        elif h == max_height:
            max_height_count += 1

    return max_height_count


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    print solve(n, ar)
