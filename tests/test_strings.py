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

    def test_strstr(self):
        self.assertEqual(strstr('hello', 'll'), 2)
        self.assertEqual(strstr('aaaaa', 'bba'), -1)
        self.assertEqual(strstr('aa', 'aaaa'), -1)
        self.assertEqual(strstr('a','a'), 0)

    def test_longest_palin_substring(self):
        self.assertEqual('aba', longest_palin_substring('babad'))
        self.assertEqual('bb', longest_palin_substring('cbbd'))
    
    def test_string_to_integer(self):
        self.assertEqual(42, string_to_integer('42'))
        self.assertEqual(-42, string_to_integer('-42'))
        self.assertEqual(0, string_to_integer('words and 987'))
        self.assertEqual(-2147483648, string_to_integer('-91283472332'))
        self.assertEqual(4193, string_to_integer('4193 with words'))
        
if __name__ == '__main__':
    unittest.main()

