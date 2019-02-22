"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        s = "baab"
        answer = "Empty String"
        self.assertEqual(answer, solve(s))

    def test_case_2(self):
        s = "aa"
        answer = "Empty String"
        self.assertEqual(answer, solve(s))


if __name__ == "__main__":
    unittest.main()
