#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/camelcase?h_r=next-challenge&h_v=zen
Level: Easy
Max Score: 15
"""


def solve(s):

    # Create a reference dict of capital letters.
    caps = dict([(i, 1) for i in list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")])

    # Count the number of capital letters in the string as the number of words.
    word_count = 0
    for c in list(s):
        if c in caps:
            word_count += 1

    # If words were detected, add a 1 to it because the first word won't have
    # begun with a capital letter.
    if word_count:
        return word_count + 1

    # If there were no words counted, but the string is not empty, there is a
    # single word in the string.
    elif s:
        return 1

    # Word count is 0 and the string is empty, so return 0.
    else:
        return 0


if __name__ == "__main__":

    # Problem input/output.
    s = raw_input().strip()
    print solve(s)
