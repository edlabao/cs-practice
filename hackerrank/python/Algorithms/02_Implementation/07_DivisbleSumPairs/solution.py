#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/taum-and-bday/problem
Level: Easy
Max Score: 25
"""


def solve(n, k, ar):

    # Initialize the number of pairs evenly divisible by k.
    answer = 0

    # Initialize a set which will contain tuples of index pairs we've
    # already seen.
    seen = set()

    for i in xrange(len(ar)):
        for j in xrange(i + 1, len(ar)):
            if (not ((i, j) in seen or (j, i) in seen)
                    and (ar[i] + ar[j]) % k == 0):
                answer += 1
                seen.add((i, j))

    return answer


if __name__ == "__main__":

    # Problem input/output.
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    ar = map(int, raw_input().strip().split(' '))
    result = solve(n, k, ar)
    print(result)
