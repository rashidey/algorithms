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

    def test_move_zeroes(self):
        self.assertEqual(move_zeroes([0,1,0,3,12]), [1,3,12,0,0])
        self.assertEqual(move_zeroes([0,1,0,0,3,12]), [1,3,12,0,0,0])

    def test_summary_ranges(self):
        self.assertEqual(summary_ranges([0,1,2,4,5,7]), ["0->2","4->5","7"])
        self.assertEqual(summary_ranges([0,2,3,4,6,8,9]), ["0","2->4","6","8->9"])

    def test_intersect_array(self):
        self.assertEqual(intersect_array([1,2,2,1], [2,2]), [2,2])
        self.assertEqual(intersect_array([4,9,5], [9,4,9,8,4]), [4,9])

    def test_third_max(self):
        self.assertEqual(third_max([3,2,1,4,6,6,4,7]), 4)

    def test_find_dissapeared(self):
        self.assertEqual(find_disappeared([4,3,2,7,8,2,3,1]), [5, 6])

    def test_max_consec(self):
        self.assertEqual(max_consecutive_ones([1,1,0,1,1,1]), 3)

    def test_find_pairs(self):
        self.assertEqual(find_pairs([3, 1, 4, 1, 5],2), 2)
        self.assertEqual(find_pairs([1, 2, 3, 4, 5],1), 4)
        self.assertEqual(find_pairs([1,3,1,5,4], 0), 1)

    def test_max_product(self):
        self.assertEqual(max_product([1,2,3]),6)
        self.assertEqual(max_product([1,2,3,4]),24)

    def test_max_average(self):
        self.assertEqual(max_average([1,12,-5,-6,50,3], 4), 12.75)
        self.assertEqual(max_average([0,4,0,3,2], 1), 4.0)

    def test_flowers(self):
        self.assertEqual(place_flowers([1,0,0,0,1],1), True)

    def test_first_missing(self):
        self.assertEqual(first_missing_positive([1,2,0]), 3)
        self.assertEqual(first_missing_positive([3,4,-1,1]), 2)
        self.assertEqual(first_missing_positive([7,8,0,0,9,11,12]), 1)
        self.assertEqual(first_missing_positive([2,4,2,1,32,0,0,-1,3,-2,22,0,3]), 5)

    def test_non_decreasing(self):
        self.assertEqual(non_decreasing_array([4,2,3]), True)

    def test_assign_cookies(self):
        self.assertEqual(assign_cookies([1,2],[1,1]), 1)

    def test_min_moves(self):
        self.assertEqual(minimum_moves([1,2,3]), 3)

    def test_next_greater(self):
        self.assertEqual(next_greater_element([4,1,2],[1,3,4,2]), [-1,3,-1])

    def test_count_candies(self):
        self.assertEqual(distribute_candies([1,1,2,2,3,3]), 3)

    def test_shortest_unsorted_subarray(self):
        self.assertEqual(shortest_unsorted([2,6,4,8,10,9,15]), 5)

    def test_set_mismatch(self):
        self.assertEqual(find_set_mismatch([1,2,2,4]), [2,3])

    def test_max_dist(self):
        self.assertEqual(max_dist([1,0,0,0,1,0,1]), 2)

    def test_degree_array(self):
        self.assertEqual(degree_array([1, 2, 2, 3, 1]), 2)
        self.assertEqual(degree_array([1,2,2,3,1,4,2]), 6)

    def test_pivot_index(self):
        self.assertEqual(pivot_index([1,7,3,6,5,6]), 3)
        self.assertEqual(pivot_index([1,2,3]), -1)

    def test_array_partition(self):
        self.assertEqual(array_partition([1,4,3,2]), 4)

    def test_lis_con(self):
        self.assertEqual(lis_continuous([1,3,5,4,7]), 3)
        self.assertEqual(lis_continuous([2,2,2,2,2,2]), 1)
        self.assertEqual(lis_continuous([1,2]), 2)

    def test_largest_twice(self):
        self.assertEqual(largest_twice([3,6,1,0]), 1)

    def test_position_largest_groups(self):
        self.assertEqual(position_large_groups('abbxxxxzzy'), [[3,6]])

    def test_find_all_duplicates(self):
        self.assertEqual(find_all_duplicates([4,3,2,7,8,2,3,1]), [2, 3])

    