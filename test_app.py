# Runs a test to ensure that app is functioning properly

import unittest
from app import ftth_checker, conversion
from test_coords import test_neighborhood, test_home, test_not_home


class TestFTTHChecker(unittest.TestCase):
    def test_conversion(self):
        self.assertEqual(conversion(test_home['lattitude']), 32.443980555555555)

    def test_ftth_checker(self):
        self.assertEqual(ftth_checker(test_neighborhood, test_home), True)
        self.assertEqual(ftth_checker(test_neighborhood, test_not_home), False)

if __name__ == '__main__':
    unittest.main()