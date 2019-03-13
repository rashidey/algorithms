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
    
    def test_longest_unique_substring(self):
        self.assertEqual(3, longest_unique_substring('abcabcbb'))
        self.assertEqual(1, longest_unique_substring('bbbbb'))
        self.assertEqual(3, longest_unique_substring('pwwkew'))
        self.assertEqual(0, longest_unique_substring(''))
        self.assertEqual(2, longest_unique_substring('au'))

    def test_zigzag_conversion(self):
        self.assertEqual(zigzag_conversion('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(zigzag_conversion('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')
        self.assertEqual(zigzag_v2('PAYPALISHIRING', 3), 'PAHNAPLSIIGYIR')
        self.assertEqual(zigzag_v2('PAYPALISHIRING', 4), 'PINALSIGYAHRPI')

    def test_count_say(self):
        self.assertEqual(count_say(3), 21)
        self.assertEqual(count_say(4), 1211)

    def test_length_last_word(self):
        self.assertEqual(length_of_last_word('hello world'), 5)
        self.assertEqual(length_of_last_word(' '), 0)
        self.assertEqual(length_of_last_word('hello world'), 5)

    def test_multiply_strings(self):
        self.assertEqual(multiply_strings('2','3'), '6')
        self.assertEqual(multiply_strings('20','3'), '60')
        self.assertEqual(multiply_strings('02','3'), '6')
        self.assertEqual(multiply_strings('2','30'), '60')
        self.assertEqual(multiply_strings('0','3'), '0')
        self.assertEqual(multiply_strings('0','0'), '0')
        self.assertEqual(multiply_strings('1','1'), '1')

if __name__ == '__main__':
    unittest.main()

