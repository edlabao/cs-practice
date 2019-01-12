"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        grades = [73, 67, 38, 33]
        answer = [75, 67, 40, 33]
        self.assertEqual(answer, solve(grades))


if __name__ == "__main__":
    unittest.main()
