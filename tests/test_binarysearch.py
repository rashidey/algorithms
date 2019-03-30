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

    