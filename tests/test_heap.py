from algorithms.heaps import *
import unittest

class TestSuite(unittest.TestCase):
    def test_kth_largest(self):
        self.assertEqual(kth_largest([3,2,1,5,6,4], 2), 5)
        self.assertEqual(kth_largest([3,2,3,1,2,4,5,5,6], 4), 4)

    def test_k_most(self):
        self.assertEqual(k_most_frequent([1,1,1,2,2,3], 2), [1,2])
