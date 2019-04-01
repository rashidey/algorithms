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

    def test_next_perm(self):
        self.assertEqual(next_permutation([1,2,3]), [1,3,2])
        self.assertEqual(next_permutation([3,2,1]), [1,2,3])
        self.assertEqual(next_permutation([1,1,5]), [1,5,1])
        self.assertEqual(next_permutation([1,3,2]), [2,1,3])

    def test_divide_two_numbers_v2(self):
        self.assertEqual(divide_two_numbers_v2(10, 2), 5)
        self.assertEqual(divide_two_numbers_v2(2342523443242523, 2), 2147483647)
        self.assertEqual(divide_two_numbers_v2(-43564356345235346324, 2), -2147483648)
        self.assertEqual(divide_two_numbers_v2(10, 3), 3)
        self.assertEqual(divide_two_numbers_v2(102, 2), 51)
        self.assertEqual(divide_two_numbers_v2(6, 2), 3)

    def test_power_of_two(self):
        self.assertEqual(power_of_two(1), True)
        self.assertEqual(power_of_two(2), True)
        self.assertEqual(power_of_two(16), True)
        self.assertEqual(power_of_two(218), False)

    def test_missing_number(self):
        self.assertEqual(missing_number([3,0,1]), 2)
        self.assertEqual(missing_number([9,6,4,2,3,5,7,0,1]), 8)

    def test_valid_number(self):
        self.assertEqual(valid_number('0'), True)
        self.assertEqual(valid_number('0.1'), True)
        self.assertEqual(valid_number('abc'), False)
        self.assertEqual(valid_number('1 a'), False)
        self.assertEqual(valid_number('2e10'), True)
        self.assertEqual(valid_number(' -90e3    '), True)
        self.assertEqual(valid_number('  1e'), False)
        self.assertEqual(valid_number('e3'), False)
        self.assertEqual(valid_number(' 6e-1'), True)
        self.assertEqual(valid_number('  99e2.5'), False)
        self.assertEqual(valid_number('53.5e93'), True)
        self.assertEqual(valid_number(' --6 '), False)
        self.assertEqual(valid_number('-+3'), False)
        self.assertEqual(valid_number('95a54e53'), False)

