"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        s1 = "cde"
        s2 = "abc"
        answer = 4
        self.assertEqual(answer, solve(s1, s2))


if __name__ == "__main__":
    unittest.main()
