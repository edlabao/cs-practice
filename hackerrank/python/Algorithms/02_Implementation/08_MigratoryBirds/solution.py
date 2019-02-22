#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/migratory-birds/problem
Level: Easy
Max Score: 10
"""


def solve(n, ar):

    # Initialize an answer list which will contain a list of all type numbers
    # that occur maxNum times. This is a list since more than one type can have
    # maxNum occurrences.
    answer = []

    # Keep track of the current maximum number of occurrences of any type.
    maxNum = 0

    # Dict with type numbers as keys and their occurrence count as values.
    types = {}

    # Iterate thru the array and record types and their number of occurrences.
    for type in ar:
        if type not in types:
            types[type] = 0
        types[type] += 1
        if types[type] > maxNum:
            maxNum = types[type]

    # We now know what the maximum number of occurrences is, so iterate thru the
    # array one more time to get the type(s) that occur maxNum times.
    for type in ar:
        if types[type] == maxNum:
            answer.append(type)

    # Return the type with the lowest value in the answer.
    return min(answer)


if __name__ == "__main__":

    # Problem input/output.
    n = int(raw_input().strip())
    ar = map(int, raw_input().strip().split(' '))
    result = solve(n, ar)
    print(result)
