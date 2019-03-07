from algorithms.strings import *
import unittest

class TestSuite(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome(121))  
        self.assertFalse(is_palindrome(-121))  
        self.assertFalse(is_palindrome(10))  
        self.assertTrue(is_palindrome(1))

    def test_reverse(self):
        self.assertEqual(321, reverse_int(123))  
        self.assertEqual(-321, reverse_int(-123))  
        self.assertEqual(21, reverse_int(120))  
        self.assertEqual(0, reverse_int(23532563245236))  
    
    def test_int_to_roman(self):
        self.assertEqual('III', int_to_roman(3))
        self.assertEqual('IV', int_to_roman(4))
        self.assertEqual('IX', int_to_roman(9))
        self.assertEqual('LVIII', int_to_roman(58))
        self.assertEqual('MCMXCIV', int_to_roman(1994))

    def test_roman_to_int(self):
        self.assertEqual(roman_to_int('III'), 3)
        self.assertEqual(roman_to_int('IV'), 4)
        self.assertEqual(roman_to_int('IX'), 9)
        self.assertEqual(roman_to_int('LVIII'), 58)
        self.assertEqual(roman_to_int('MCMXCIV'), 1994)

    def test_longest_common_prefix(self):
        self.assertEqual('fl', longest_common_prefix(["flower","flow","flight"]))
        self.assertEqual('', longest_common_prefix(['dog', 'racercar', 'car']))

if __name__ == '__main__':
    unittest.main()

