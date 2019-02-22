"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        n = 5
        s = map(int, "1 2 1 3 2".strip().split(" "))
        d = 3
        m = 2
        answer = 2
        self.assertEqual(answer, solve(n, s, d, m))

    def test_case_2(self):
        n = 6
        s = map(int, "1 1 1 1 1 1".strip().split(" "))
        d = 3
        m = 2
        answer = 0
        self.assertEqual(answer, solve(n, s, d, m))


if __name__ == "__main__":
    unittest.main()
