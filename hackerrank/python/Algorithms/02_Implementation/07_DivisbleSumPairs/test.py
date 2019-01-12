"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        n = 6
        k = 3
        ar = [1, 3, 2, 6, 1, 2]
        answer = 5
        self.assertEqual(answer, solve(n, k, ar))


if __name__ == "__main__":
    unittest.main()
