"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        s = "AAAA"
        answer = 3
        self.assertEqual(answer, solve(s))

    def test_case_2(self):
        s = "BBBBB"
        answer = 4
        self.assertEqual(answer, solve(s))

    def test_case_3(self):
        s = "ABABABAB"
        answer = 0
        self.assertEqual(answer, solve(s))

    def test_case_4(self):
        s = "BABABA"
        answer = 0
        self.assertEqual(answer, solve(s))

    def test_case_5(self):
        s = "AAABBB"
        answer = 4
        self.assertEqual(answer, solve(s))


if __name__ == "__main__":
    unittest.main()
