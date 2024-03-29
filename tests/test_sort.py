import unittest, copy
import random
from algorithms.sort import *

class TestSetup(unittest.TestCase):

    def setUp(self):
        arrays = list()
        for i in range(10):
            temp = []
            for i in range(i):
                temp.append(random.randrange(-10000, 10000))
            arrays.append(temp)
        self.nums = arrays

class TestSuite(TestSetup):

    def test_selection_sort(self):
        for nums in self.nums:
            self.assertEqual(selection_sort(nums), sorted(nums))

    def test_bubble_sort(self):
        for nums in self.nums:
            self.assertEqual(bubble_sort(nums), sorted(nums))

    def test_insertion_sort(self):
        for nums in self.nums:
            self.assertEqual(insertion_sort(nums), sorted(nums))

    def test_merge_sort(self):
        for nums in self.nums:
            nums_copy = nums
            merge_sort(nums)
            self.assertEqual(nums_copy, sorted(nums))

    def test_quick_sort(self):
        for nums in self.nums:
            nums_copy = nums 
            quick_sort(nums_copy, 0, len(nums) - 1)
            self.assertEqual(nums_copy, sorted(nums))

    def test_sort_colors(self):
        nums = [2,0,2,1,1,0]
        self.assertEqual(sort_colors(nums), sorted(nums))

    def test_max_profit(self):
        self.assertEqual(max_profit_worker([2,4,6,8,10], [10,20,30,40,50],[4,5,6,7]), 100)

    def test_sort_parity(self):
        self.assertEqual(sort_array_parity([3,1,2,4]), [4,2,1,3])