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

    def test_subsets(self):
        self.assertEqual(subsets([1,2,3]), [[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]])
        self.assertEqual(subsets_duplicates([1,2,2]), [[],[1],[1,2],[1,2,2],[2],[2,2]])

    def test_combinations_sum(self):
        self.assertEqual(combinations_sum([2,3,6,7], 7), [[2,2,3],[7]])
        self.assertEqual(combinations_sum([2,3,5], 8), [[2,2,2,2],[2,3,3],[3,5]])

    def test_combinations_sum_two(self):
        self.assertEqual(combinations_sum_two([2,5,2,1,2], 5), [[1,2,2],[5]])

    def test_generate_paran(self):
        self.assertEqual(generate_paran(3), ["((()))","(()())","(())()","()(())","()()()"])
    
    def test_combination_numbers(self):
        self.assertEqual(combinations_numbers(4, 2), [[1,2],[1,3],[1,4], [2,3],[2,4],[3,4]])
        self.assertEqual(combinations_numbers(4,4), [[1,2,3,4]])
