#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/sock-merchant/problem
Level: Easy
Max Score: 10
"""


def solve(n, ar):

    answer = 0

    # Create a hash with the sock color code as the key and the number of socks
    # with this color as the value.
    pairs = {}
    for s in ar:
        if s not in pairs:
            pairs[s] = 0
        pairs[s] += 1

    # Go thru the pairs hash and find out how many pairs we have.
    for num in pairs.itervalues():
        answer += num / 2

    return answer


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))

    result = solve(n, ar)
    print(result)
