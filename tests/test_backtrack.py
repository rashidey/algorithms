from algorithms.backtrack import *
import unittest

class TestSuite(unittest.TestCase):
    def test_letter_combinations(self):
        self.assertEqual(letter_combinations('23'), ["ad", "ae", "af", "bd", 
                                                   "be", "bf", "cd", "ce", "cf"])
