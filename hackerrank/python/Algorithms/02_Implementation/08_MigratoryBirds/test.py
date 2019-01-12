"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        n = 6
        ar = [1, 4, 4, 4, 5, 3]
        answer = 4
        self.assertEqual(answer, solve(n, ar))


if __name__ == "__main__":
    unittest.main()
