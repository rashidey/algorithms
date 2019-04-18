from algorithms.dp import *
import unittest

class TestSuite(unittest.TestCase):
    def test_pascal(self):
        self.assertEqual(pascal(1), [[1]])
        self.assertEqual(pascal(2), [[1], [1,1]])
        self.assertEqual(pascal(3), [[1], [1,1], [1,2,1]])
        self.assertEqual(pascal(4), [[1], [1,1], [1,2,1],[1,3,3,1]])

    def test_pascal_row(self):
        self.assertEqual(pascal_row(1), [1])
        self.assertEqual(pascal_row(2), [1,1])
        self.assertEqual(pascal_row(3), [1,2,1])
        self.assertEqual(pascal_row(4), [1,3,3,1])

    def test_fibonacci(self):
        self.assertEqual(fibonacci_recursive(1), 1)
        self.assertEqual(fibonacci_dynamic(1), 1)
        self.assertEqual(fibonacci_dynamic_v2(1), 1)
        self.assertEqual(fibonacci_formula(10), 89)

    def test_climb_stairs(self):
        self.assertEqual(climbing_stairs(3), 3)

    def test_power(self):
        self.assertEqual(pow_v3(2,3), 8)
        self.assertEqual(pow_v3(2,-3), 0.125)

    def test_lcs(self):
        self.assertEqual(lcs('bd', 'abcd'), 2)
        self.assertEqual(lcs('aggtab', 'gxtxayb'), 4)
        self.assertEqual(lcs_dp('bd', 'abcd'), 2)
        self.assertEqual(lcs_dp('aggtab', 'gxtxayb'), 4)

    def test_min_dist(self):
        self.assertEqual(min_distance_strings('seab', 'eat'), 3)
        self.assertEqual(min_distance_strings('sea', 'eat'), 2)

    def test_lis(self):
        self.assertEqual(longest_inc([10,9,2,5,3,7,101,18]), 4)

    def test_triangle(self):
        triangle = [[2],
                    [3,4],
                    [6,5,7],
                    [4,1,8,3]]
        self.assertEqual(triangle_min_path(triangle), 11)

    def test_unique_paths(self):
        self.assertEqual(unique_paths(3,2), 3)
        self.assertEqual(unique_paths(7,3), 28)

    def test_unique_obstacles(self):
        grid = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(unique_paths_two(grid), 2)

    def test_min_grid_sum(self):
        grid = [[1,3,1],[1,5,1],[4,2,1]]
        self.assertEqual(minimum_path_sum(grid), 7)

    def test_zero_matrix(self):
        matrix = [[0,0,0],[0,1,0],[0,0,0]]
        result = [[0,0,0],[0,1,0],[0,0,0]]
        self.assertEqual(zero_matrix(matrix), result)

    def test_house_robber(self):
        self.assertEqual(house_robber_v1([1,2,3,1]), 4)
        self.assertEqual(house_robber_v1([2,7,9,3,1]), 12)
        self.assertEqual(house_robber_v2([1,2,3,1]), 4)
        self.assertEqual(house_robber_v2([2,7,9,3,1]), 12)
        self.assertEqual(house_robber_v3([1,2,3,1]), 4)
        self.assertEqual(house_robber_v3([2,7,9,3,1]), 12)
        self.assertEqual(house_robber_v4([1,2,3,1]), 4)
        self.assertEqual(house_robber_v4([2,7,9,3,1]), 12)

    def test_range_sum(self):
        nums = [-2,0,3,-5,2,-1]
        num_array = NumArray(nums)
        self.assertEqual(num_array.sum_range(0,2), 1)
        self.assertEqual(num_array.sum_range(2,5), -1)
        self.assertEqual(num_array.sum_range(0,5), -3)

    def test_cost(self):
        self.assertEqual(min_cost_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]), 6)

    def test_subarray_sum(self):
        self.assertEqual(subarray_sum([1,5], -6), True)

    def test_integer_replacement(self):
        self.assertEqual(integer_replacement(8), 3)
        self.assertEqual(integer_replacement(7), 4)