#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/two-characters/problem
Level: Easy
Max Score: 15
"""


def is_interleaved(c1, c2, chars):
    """
    Return True if the character index lists given by characters c1 qnd c2 are
    interleaved, False otherwise.
    """

    answer = True

    # Reference the character index lists and determine which one should go
    # first, i.e. which list has the smaller first element and make that list1.
    list1 = chars[c1]
    list2 = chars[c2]

    if list1[0] > list2[0]:
        list1 = chars[c2]
        list2 = chars[c1]

    # For the characters to be interleaved, their counts can't differ by more
    # than 1.
    if abs(len(list1) - len(list2)) > 1:
        answer = False

    # In addition, the first list can't be smaller than the second list or there
    # would not be enough characters to be properly interleaved.
    elif len(list1) < len(list2):
        answer = False

    else:
        # Now actually determine if the lists are interleaved by comparing
        # adjacently indexed elements in list1 and list2. We start at index 1,
        # since we've already looked at index 0.
        idx = 1
        while idx < len(list1) and idx < len(list2):

            # The element at the current index of list1 should be less than
            # that of list2. In addition, the previous element in list2 should
            # be less than the current element in list1. If either of these
            # aren't true, the lists aren't interleaved.
            if list1[idx] > list2[idx] or list1[idx] < list2[idx - 1]:
                answer = False
                break

            idx += 1

    return answer


def solve(s):

    # Our answer is th length of the largest string of alternating characters.
    answer = 0

    chars = {}
    idx = 0

    # Scan the string and track the unique characters and the indexex at which
    # they appear in a dict called chars.
    for c in s:
        if c not in chars:
            chars[c] = []
        chars[c].append(idx)
        idx += 1

    # Compare every character against every other.
    for c1 in chars:
        for c2 in chars:
            if c1 != c2 and is_interleaved(c1, c2, chars):
                # If this looks like a valid interleaving sequence of two
                # characters, record it's length if it's greater than our
                # current answer.
                if len(chars[c1]) + len(chars[c2]) > answer:
                    answer = len(chars[c1]) + len(chars[c2])

    return answer


if __name__ == "__main__":

    # Problem input/output.
    s_len = int(raw_input().strip())
    s = raw_input().strip()
    print solve(s)
