#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/the-hurdle-race/problem
Level: Easy
Max Score: 15
"""


def solve(n, k, b, ar):

    # Initialize the return answer which will be the amount that Anna was
    # overcharged.
    answer = 0

    # Determine what Anna really owes by iterating thru the item prices and
    # adding all but the kth item then dividing the sum by 2.
    total = 0
    idx = 0
    while idx < len(ar):
        if idx != k:
            total += ar[idx]
        idx += 1

    # Anna owes half the total. If this is more than what she paid, b, then
    # she was overcharged by (b - owed).
    owed = total / 2
    if owed < b:
        answer = b - owed

    # If Anna was overcharged, return the amount, otherwise, return the string
    # "Bon Appetit"
    if answer:
        return answer
    else:
        return "Bon Appetit"


if __name__ == "__main__":

    # Problem input/output.
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    ar = map(int, raw_input().strip().split(' '))
    b = int(raw_input().strip())

    result = solve(n, k, b, ar)
    print(result)
