#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/reduced-string/problem
Level: Easy
Max Score: 10
"""


def solve(s):
    """
    Walk thru the string, comparing two characters at a time. Add characters
    that are not adjacent duplicates to our results.
    """
    answer = []
    string = list(s)

    # Initialize the index we'll use to walk thru the string.
    idx = 0

    # We index idx+1 to get the next character in the string, so our loop
    # condition should make sure idx+1 is less than the total string length.
    while (idx + 1) < len(string):

        # Compare the last char we put into the result with the current char. If
        # They are the same, remove the last char from result and skip the
        # current char.
        if answer and (answer[-1] == string[idx]):
            answer.pop()
            idx += 1

        # Compare the char at the current index and the char after it. If they
        # are not the same, add the char at the current index to our result.
        elif string[idx] != string[idx + 1]:
            answer.append(string[idx])
            idx += 1
        else:
            idx += 2

    if idx < len(string):
        if answer and answer[-1] == string[-1]:
            answer.pop()
        else:
            answer.append(string[-1])

    # Return the result string, or if it is empty, return "Empty String" as per
    # the problem requirements.
    if answer:
        return "".join(answer)
    else:
        return "Empty String"


if __name__ == "__main__":

    # Problem input/output.
    s = raw_input().strip()
    result = solve(s)
    print(result)
