"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        n = 9
        ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
        answer = 3
        self.assertEqual(answer, solve(n, ar))


if __name__ == "__main__":
    unittest.main()
