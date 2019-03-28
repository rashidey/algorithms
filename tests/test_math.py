from algorithms.math import *
import unittest

class TestSuite(unittest.TestCase):
    def test_add_binary(self):
        self.assertEqual(add_binary('11', '1'), '100')
        self.assertEqual(add_binary('1010', '1011'), '10101')
        self.assertEqual(add_binary('0', '0'), '0')
        self.assertEqual(add_binary('011', '1'), '100')
        self.assertEqual(add_binary('101', '1'), '110')

    def test_divide_two(self):
    	self.assertEqual(divide_two_numbers(3, -3), -1)

    def test_happy_number(self):
    	self.assertEqual(happy_numbers(19), True)
    	self.assertEqual(happy_numbers(191), False)

    def test_count_primes(self):
        self.assertEqual(count_primes(10), 4)

    def test_convert_to_title(self):
        self.assertEqual(convert_to_title(1), 'A')
        self.assertEqual(convert_to_title(28), 'AB')
        self.assertEqual(convert_to_title(701), 'ZY')

    def test_convert_to_number(self):
        self.assertEqual(convert_to_number('A'), 1)
        self.assertEqual(convert_to_number('AB'), 28)
        self.assertEqual(convert_to_number('ZY'), 701)

    def test_majority_element(self):
        self.assertEqual(majority_element([3,2,3]), 3)
        self.assertEqual(majority_element([2,2,1,1,1,2,2]), 2)