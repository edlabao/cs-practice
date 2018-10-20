#!/usr/bin/env python

"""
Problem URL: https://www.hackerrank.com/challenges/time-conversion/problem
Level: Easy
Score: 15

Example:
07:05:45PM
> 19:05:45
"""

import datetime


def solve(s):
    """
    Convert the input time in the format "hh:mm:ss[AM|PM]" to 24-hour format.
    """
    # Just use python's datetime library to input the string and convert it to
    # a datetime object, then use the datetime object to return a string in
    # 24-hour format.
    dt = datetime.datetime.strptime(s, "%I:%M:%S%p")
    return dt.strftime("%H:%M:%S")


if __name__ == "__main__":

    # Problem input/output.
    s = raw_input().strip()
    print solve(s)
