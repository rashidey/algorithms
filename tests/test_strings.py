from algorithms.strings import *
import unittest

class TestSuite(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(isPalindrome(121))  
        self.assertFalse(isPalindrome(-121))  
        self.assertFalse(isPalindrome(10))  
        self.assertTrue(isPalindrome(1))

    def test_reverse(self):
        self.assertEqual(321, reverseInt(123))  
        self.assertEqual(-321, reverseInt(-123))  
        self.assertEqual(21, reverseInt(120))  
        self.assertEqual(0, reverseInt(23532563245236))  
    
    def test_int_to_roman(self):
        self.assertEqual('III', intToRoman(3))
        self.assertEqual('IV', intToRoman(4))
        self.assertEqual('IX', intToRoman(9))
        self.assertEqual('LVIII', intToRoman(58))
        self.assertEqual('MCMXCIV', intToRoman(1994))

    def test_roman_to_int(self):
        self.assertEqual(romanToInt('III'), 3)
        self.assertEqual(romanToInt('IV'), 4)
        self.assertEqual(romanToInt('IX'), 9)
        self.assertEqual(romanToInt('LVIII'), 58)
        self.assertEqual(romanToInt('MCMXCIV'), 1994)

    def test_longest_common_prefix(self):
        self.assertEqual('fl', longestCommonPrefix(["flower","flow","flight"]))
        self.assertEqual('', longestCommonPrefix(['dog', 'racercar', 'car']))

if __name__ == '__main__':
    unittest.main()

