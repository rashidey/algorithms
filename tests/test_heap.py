from algorithms.heaps import *
import unittest

class TestSuite(unittest.TestCase):
    def test_kth_largest(self):
        self.assertEqual(kth_largest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)

    def test_k_most(self):
        self.assertEqual(k_most_frequent([1,1,1,2,2,3], 2), [1,2])

    def test_kth_largest(self):
        k = 3
        nums = [4,5,8,2]
        kth_largest = KthLargest(k, nums)
        self.assertEqual(kth_largest.add(3), 4)
        self.assertEqual(kth_largest.add(5), 5)
        self.assertEqual(kth_largest.add(10), 5)
        self.assertEqual(kth_largest.add(9), 8)
        self.assertEqual(kth_largest.add(4), 8)

    def test_kth_smallest(self):
        matrix = matrix = [[ 1,  5,  9],[10, 11, 13],[12, 13, 15]]
        self.assertEqual(kth_smallest_matrix(matrix, 8), 13)

    def test_kth_pairs(self):
        self.assertEqual(k_smallest_pairs([1,2],[3], 3), [[1,3],[2,3]])

    def test_top_words(self):
        self.assertEqual(top_k_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2), ['i', 'love'])
        