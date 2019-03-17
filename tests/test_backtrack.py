from algorithms.backtracking import *
import unittest

class TestSuite(unittest.TestCase):
    def test_letter_combinations(self):
        self.assertEqual(letter_combinations('23'), ["ad", "ae", "af", "bd", 
                                                   "be", "bf", "cd", "ce", "cf"])

    def test_permute(self):
        self.assertEqual(permute([1,2,3]), [[1,2,3], [1,3,2], [2,1,3],
                                          [2,3,1], [3,1,2], [3,2,1]])

    def test_permute_two(self):
        self.assertEqual(permute_unique([1,1,2]), [[1,2,1],[2,1,1],[1,1,2]])
        self.assertEqual(permute_unique_v2([1,1,2]), [[1,1,2],[1,2,1],[2,1,1]])