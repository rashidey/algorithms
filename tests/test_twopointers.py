from algorithms.twopointers import *
import unittest

class TestSuite(unittest.TestCase):
    def test_remove_duplicates(self):
        self.assertEqual(remove_duplicates([0,0,1,1,1,2,2,3,3,4]), 5)
        self.assertEqual(remove_duplicates([1,1,2]), 2)

    def test_remove_element(self):
        self.assertEqual(remove_element([3,2,2,3], 3), 2)
        self.assertEqual(remove_element([0,1,2,2,3,0,4,2], 2), 5)
    
    def test_three_sum(self):
        self.assertEqual(three_sum_closest([-1,2,1,-4], 1), 2)
        self.assertEqual(three_sum_closest([1,2,3,4,5,6,7,8,9,10], 27), 27)

    def test_max_water(self):
        self.assertEqual(max_area_water([1,8,6,2,5,4,8,3,7]), 49)

    def test_find_duplicates(self):
        self.assertEqual(find_duplicate([1,3,4,2,2]), 2)

    def test_longest_word_in_dict(self):
        self.assertEqual(longest_word_dict('abpcplea', ["ale","apple","monkey","plea"]), 'apple')

    def test_character_replacement(self):
        self.assertEqual(character_replacement('ABAB', 2), 4)

    def test_sorted_array(self):
        self.assertEqual(sorted_squares([-4,-1,0,3,10]), [0,1,9,16,100])

    