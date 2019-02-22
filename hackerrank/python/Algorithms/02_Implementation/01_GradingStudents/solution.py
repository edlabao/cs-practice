#!/usr/bin/env python

"""
Problem: https://www.hackerrank.com/challenges/grading/problem
Level: Easy
Max Score: 10
"""


def solve(grades):
    """
    Return grades rounded up to nearest 5 if above 38, otherwise, do not round
    the score.
    """

    rounded_grades = []
    for grade in grades:
        if grade >= 38:
            rounded = ((grade + 5) / 5) * 5
            if rounded - grade < 3:
                grade = rounded
        rounded_grades.append(grade)

    return rounded_grades


if __name__ == "__main__":

    # Problem input and output
    n = int(raw_input().strip())
    grades = []
    grades_i = 0
    for grades_i in xrange(n):
        grades_t = int(raw_input().strip())
        grades.append(grades_t)

    result = solve(grades)
    print "\n".join(map(str, result))
