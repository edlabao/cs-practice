"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        s = "saveChangesInTheEditor"
        answer = 5
        self.assertEqual(answer, solve(s))


if __name__ == "__main__":
    unittest.main()
