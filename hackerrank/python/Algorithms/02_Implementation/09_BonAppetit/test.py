"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        n = 4
        k = 1
        ar = [3, 10, 2, 9]
        b = 12
        answer = 5
        self.assertEqual(answer, solve(n, k, b, ar))

    def test_case_2(self):
        n = 4
        k = 1
        ar = [3, 10, 2, 9]
        b = 7
        answer = "Bon Appetit"
        self.assertEqual(answer, solve(n, k, b, ar))


if __name__ == "__main__":
    unittest.main()
