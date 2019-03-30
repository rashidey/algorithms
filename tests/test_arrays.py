from algorithms.arrays import *
import unittest

class TestSuite(unittest.TestCase):
    def test_add_one(self):
        self.assertEqual(plus_one([1,2,3]), [1,2,4])
        self.assertEqual(plus_one([4,3,2,1]), [4,3,2,2])
        self.assertEqual(plus_one([9,9,9,9]), [1,0,0,0,0])
        self.assertEqual(plus_one([8,9,9,9]), [9,0,0,0])
        self.assertEqual(plus_one([0]), [1])
        self.assertEqual(plus_one([1, 0]), [1, 1])

    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates_two([1,1,1,2,2,3]), 5)
        self.assertEqual(remove_duplicates_two([0,0,1,1,1,1,2,3,3]), 7)

    def test_merge_sorted(self):
        self.assertEqual(merge_sorted([1,2,3,0,0,0],3,[2,5,6],3), [1,2,2,3,5,6])

    def test_number_plus_one(self):
        self.assertEqual(plus_one([1,2,3]), [1,2,4])
        self.assertEqual(plus_one([4,3,2,1]), [4,3,2,2])

    def test_rotate_array(self):
        self.assertEqual(rotate_array([1,2,3,4,5,6,7], 3), [5,6,7,1,2,3,4])

    def test_contains_duplicates(self):
        self.assertEqual(contains_duplicates([1,2,3,1]), True)

    def test_merge_intervals(self):
        self.assertEqual(merge_intervals([[1,3],[2,6],[8,10],[15,18]]), [[1,6],[8,10],[15,18]])
        self.assertEqual(merge_intervals([[1,4],[4,5]]), [[1,5]])