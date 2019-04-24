from algorithms.binarysearch import *
import unittest

class TestSuite(unittest.TestCase):
    def test_search_insert_position(self):
        self.assertEqual(search_insert_position([1,3,5,6], 5), 2)
        self.assertEqual(search_insert_position([1,3,5,6], 2), 1)
        self.assertEqual(search_insert_position([1,3,5,6], 7), 4)
        self.assertEqual(search_insert_position([1,3,5,6], 0), 0)

    def test_square(self):
         self.assertEqual(valid_square(16), True)
         self.assertEqual(valid_square(14), False)

    def test_binary_search(self):
        self.assertEqual(binary_search([1,2,3,4,5], 3), 2)

    def test_sqrt_number(self):
        self.assertEqual(sqrt_number(16), 4)
        self.assertEqual(sqrt_number(14), 3)
        self.assertEqual(sqrt_number(26), 5)

    def test_game_guess(self):
        game = GuessGame(6, 10)
        result = game.guess_number()
        self.assertEqual(result, game.pick)
        game = GuessGame(11, 10)
        result = game.guess_number()
        self.assertEqual(result, -1)
        game = GuessGame(0, 10)
        result = game.guess_number()
        self.assertEqual(result, game.pick)
        game = GuessGame(2, 10)
        result = game.guess_number()
        self.assertEqual(result, game.pick)

    def test_search_rotated(self):
        self.assertEqual(search_rotated([4,5,6,0,1,2], 8), -1)
        self.assertEqual(search_rotated([4,5,6,0,1,2], 0), 3)

    def test_first_bad_version(self):
        self.assertEqual(first_bad(150), 100)
        self.assertEqual(first_bad(150), 100)

    def tes_peak_find(self):
        self.assertEqual(find_peak([1,2,3,1]), 2)
        self.assertEqual(find_peak([1,2,1,3,5,6,4]), 5)

    def test_search_range(self):
        self.assertEqual(search_range([1,2,3,4,4,4], 4), [3,5])
        self.assertEqual(search_range([1,1], 0), [-1,-1])

    def test_find_k_closest(self):
        self.assertEqual(find_k_closest([1,2,3,4,5], 4, 3), [1,2,3,4])
        self.assertEqual(find_k_closest([1,2,3,4,5], 4, -1), [1,2,3,4])
        self.assertEqual(find_k_closest([1],1,1), [1])
        self.assertEqual(find_k_closest([0,0,1,2,3,3,4,7,7,8],3,5), [3,3,4])

    def test_find_min_rotated(self):
        self.assertEqual(find_min_rotated([3,4,5,1,2]), 1)
        self.assertEqual(find_min_rotated([4,5,6,7,0,1,2]), 0)

    def test_search_2d(self):
        matrix = [[1,   3,  5,  7],[10, 11, 16, 20],[23, 30, 34, 50]]
        self.assertEqual(search_matrix(matrix, 3), True)
        self.assertEqual(search_matrix(matrix, 5), True)
        self.assertEqual(search_matrix(matrix, 20), True)
        self.assertEqual(search_matrix(matrix, 31), False)

    def test_arraning_coins(self):
        self.assertEqual(arranging_coins(5), 2)
        self.assertEqual(arranging_coins(8), 3)
        self.assertEqual(arranging_coins(1804289383), 60070)

    def test_mountain(self):
        self.assertEqual(mountain_array([0,1,0]), 1)
        self.assertEqual(mountain_array([0,2,1,0]), 1)
        self.assertEqual(mountain_array([1,2,3,4,5]), -1)

    def test_sorted_rotated(self):
        self.assertEqual(sorted_array_rotated_duplicates([2,5,6,0,0,1,2], 0), True)