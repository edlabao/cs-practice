#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/making-anagrams/problem
Level: Easy
Max Score: 30
"""


def solve(s1, s2):

    # Initialize the answer which is the number of deletions we need to make to
    # make the two strings anagrams of each other.
    answer = 0

    # Process the two strings into dictionaries containing character frequencies
    # found in each.
    d1 = {}
    for c in s1:
        if c not in d1:
            d1[c] = 0
        d1[c] += 1

    d2 = {}
    for c in s2:
        if c not in d2:
            d2[c] = 0
        d2[c] += 1

    # First, we remove the characters that are different between the strings
    # from the dictionaries. One simple way to do this is with a
    # set.difference() operation. We need to do a two-way comparison tho so
    # take the union of the 2 set diffs.
    for c in set(s1).difference(set(s2)).union(set(s2).difference(set(s1))):

        # The number of deletions to remove the current character is the number
        # of times it occurs which is simply the value of the character key in
        # the dict. The difference operation doesn't tell us which dict the
        # character is in, so check both if necessary.
        if c in d1:
            answer += d1.pop(c)
        else:
            answer += d2.pop(c)

    # Now we also have to make sure that there are the same number of
    # occurrences of common characters. If not, the excess will have to be
    # deleted.
    for c in d1.iterkeys():
        answer += abs(d1[c] - d2[c])

    return answer


if __name__ == "__main__":

    # Problem input/output.
    s1 = raw_input().strip()
    s2 = raw_input().strip()
    result = solve(s1, s2)
    print(result)
