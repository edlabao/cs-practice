#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/the-birthday-bar/problem
Level: Easy
Max Score: 10
"""


def list_sum(alist):
    """
    Helper function to return the sum of all elements in the given list.
    """
    sum = 0
    for i in alist:
        sum += i
    return sum


def solve(n, s, d, m):

    answer = 0

    # Iterate thru the list m elements at a time and check if the sum of each
    # sub-list equals d.
    for i in xrange(n):
        if list_sum(s[i:i + m]) == d:
            answer += 1

    return answer


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    s = map(int, raw_input().strip().split(' '))
    d, m = raw_input().strip().split(' ')
    d, m = [int(d), int(m)]
    result = solve(n, s, d, m)
    print(result)
