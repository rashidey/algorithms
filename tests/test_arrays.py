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

    def test_contains_duplicate_two(self):
        self.assertEqual(contains_duplicate_range([1,2,3,1], 3), True)
        self.assertEqual(contains_duplicate_range([1,0,1,1], 1), True)
        self.assertEqual(contains_duplicate_range([1,2,3,1,2,3], 2), False)
        self.assertEqual(contains_duplicate_range([99,99], 2), True)

    def test_max_array(self):
        self.assertEqual(maximum_subarray([-2,1,-3,4,-1,2,1,-5,4]), 6)
        self.assertEqual(maximum_subarray([-1]), -1)

    def test_two_sum_sorted(self):
        self.assertEqual(two_sum_sorted([2,7,11,15], 9), [1,2])
        self.assertEqual(two_sum_sorted([2,7,11,15], 26), [3,4])
        self.assertEqual(two_sum_sorted([2,7,11,15], 264), [])

    def test_stock_buy(self):
        self.assertEqual(max_profit_stock([7,1,5,3,6,4]), 5)
        self.assertEqual(max_profit_stock([7,6,4,3,1]), 0)

    def test_stock_sell(self):
        self.assertEqual(max_profit_all([7,1,5,3,6,4]), 7)
        self.assertEqual(max_profit_all([1,2,3,4,5]), 4)
        self.assertEqual(max_profit_all([7,6,4,3,1]), 0)