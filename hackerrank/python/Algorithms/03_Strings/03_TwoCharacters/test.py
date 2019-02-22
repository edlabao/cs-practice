"""
Run the test cases for the excercise as unittests.
"""

import unittest

from solution import solve


class Test(unittest.TestCase):

    def test_case_1(self):
        s = "beabeefeab"
        answer = 5
        self.assertEqual(answer, solve(s))

    def test_case_8(self):
        s = "uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprel" \
            + "bayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthov" \
            + "pjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswts" \
            + "ogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixc" \
            + "hfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnml" \
            + "zogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsg" \
            + "frevzon"
        answer = 0
        self.assertEqual(answer, solve(s))


if __name__ == "__main__":
    unittest.main()
