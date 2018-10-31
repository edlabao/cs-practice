"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        a = 2
        b = 4
        answer = 6
        self.assertEqual(answer, solve(a, b))


if __name__ == "__main__":
    unittest.main()
