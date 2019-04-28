from algorithms.hashtables import *
import unittest

class TestSuite(unittest.TestCase):
    def test_two_sum(self):
        self.assertEqual([0, 1], two_sum([2,7,11,15], 9))
        self.assertEqual([0, 2], two_sum([2,7,11,15], 13))
        self.assertEqual([0, 3], two_sum([2,7,11,15], 17))
        self.assertEqual([0, 1], two_sum([2,7], 9))
        self.assertEqual([0, 1], two_sum([11,15], 26))
        self.assertEqual([1, 2], two_sum([12, 54,1,5,2,7,11,15], 55))
        self.assertEqual([3, 4], two_sum([2,7,11,3,65,15], 68))

    def test_three_sum(self):
        self.assertEqual(three_sum([-1,0,1,2,-1,-4]), [[-1,-1,2], [-1,0,1]])
        self.assertEqual(three_sum([-2,0,1,1,2]), [[-2, 0, 2], [-2, 1, 1]])
        self.assertEqual(three_sum([0,0,0,0]), [[0,0,0]])

    def test_four_sum(self):
        self.assertEqual(four_sum([1, 0, -1, 0, -2, 2], 0),
                                [(-1,  0, 0, 1),(-2,  0, 0, 2),(-2, -1, 1, 2)])

    def test_substring_concat(self):
        self.assertEqual(substring_concat('barfoothefoobarman', ['foo', 'bar']), [0, 9])
        self.assertEqual(substring_concat('wordgoodgoodgoodbestword', 
                                            ["word","good","best","word"]), [])

    def test_valid_sudoku(self):
        self.assertEqual(valid_sudoku([["5","3",".",".","7",".",".",".","."],
                                       ["6",".",".","1","9","5",".",".","."],
                                       [".","9","8",".",".",".",".","6","."],
                                       ["8",".",".",".","6",".",".",".","3"],
                                       ["4",".",".","8",".","3",".",".","1"],
                                       ["7",".",".",".","2",".",".",".","6"],
                                       [".","6",".",".",".",".","2","8","."],
                                       [".",".",".","4","1","9",".",".","5"],
                                       [".",".",".",".","8",".",".","7","9"]]), True)

        self.assertEqual(valid_sudoku([["8","3",".",".","7",".",".",".","."],
                                       ["6",".",".","1","9","5",".",".","."],
                                       [".","9","8",".",".",".",".","6","."],
                                       ["8",".",".",".","6",".",".",".","3"],
                                       ["4",".",".","8",".","3",".",".","1"],
                                       ["7",".",".",".","2",".",".",".","6"],
                                       [".","6",".",".",".",".","2","8","."],
                                       [".",".",".","4","1","9",".",".","5"],
                                       [".",".",".",".","8",".",".","7","9"]]), False)

    def test_hash_map(self):
        hashmap = HashTable()
        hashmap[1] = 1
        hashmap[11] = 2
        hashmap[21] = 3
        hashmap[31] = 4
        self.assertEqual(str(hashmap), '(1, 1) (11, 2) (21, 3) (31, 4) ')
        del hashmap[11]
        self.assertEqual(str(hashmap), '(1, 1) (21, 3) (31, 4) ')
        hashmap[31] = 4
        hashmap[2] = 4
        hashmap[3] = 4
        hashmap[4] = 4
        hashmap[5] = 4
        self.assertEqual(str(hashmap), '(1, 1) (21, 3) (2, 4) (3, 4) (4, 4) (5, 4) (31, 4) ')
        self.assertEqual(hashmap[5], 4)
        self.assertEqual(len(hashmap), 7)

    def test_group_anagrams(self):
        words = ["eat", "tea", "tan", "ate", "nat", "bat"]
        result = group_anagrams(words)
        self.assertEqual(len(result), 3)

    def test_word_pattern(self):
        self.assertEqual(word_pattern('abba', 'dog cat cat dog'), True)
        self.assertEqual(word_pattern('abba', 'dog cat cat fish'), False)
        self.assertEqual(word_pattern('aaaa', 'dog cat cat dog'), False)
        self.assertEqual(word_pattern('abba', 'dog dog dog dog'), False)

    def test_dna(self):
        self.assertEqual(len(repeated_dna('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')), 2)
        self.assertEqual(len(repeated_dna('AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT')), 2)

    def test_bulls(self):
        self.assertEqual(get_hint('1807', '7810'), '1A3B')
        self.assertEqual(get_hint('1123', '0111'), '1A1B')

    def test_find_words(self):
        self.assertEqual(find_word_rows(["Hello","Alaska","Dad","Peace", "QWERT"]),
                                        ["Alaska","Dad","QWERT"])

    def test_min_lists(self):
        list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
        list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"] 
        self.assertEqual(minimum_lists(list1, list2), ['Shogun'])

    def test_banned_words(self):
        self.assertEqual(banned_words(['hit'], "Bob hit a ball, the hit BALL flew far after it was hit."), 'ball')

    def test_subdomain(self):
        self.assertEqual(len(subdomain_visit(["9001 discuss.leetcode.com"])), 3)
    
    def test_uncommon_words(self):
        self.assertEqual(uncommon_words('apple apple', 'banana'), ['banana'])

    def test_shortest_completing_word(self):
        self.assertEqual(shortest_completing_word('1s3 PSt', ['step', 'steps', 'stripe', 'stepple']), 'steps')

    def test_is_alien(self):
        self.assertEqual(is_alien(['hello', 'leetcode'], 'hlabcdefgijkmnopqrstuvwxyz'), True)

    def test_common_chars(self):
        self.assertEqual(common_chars(["bella","label","roller"]), ['e', 'l', 'l'])
        self.assertEqual(common_chars(['cool', 'lokc', 'cook']), ['c', 'o'])

    def test_fraction_to_decimal(self):
        self.assertEqual(fraction_to_decimal(2, 3), '0.(6)')

    def test_frequency_sort(self):
        self.assertEqual(frequency_sort('bbaaaa'), 'aaaabb')

    def test_magic_dictionary(self):
        obj = MagicDictionary()
        obj.buildDict(['hello', 'leetcode'])
        self.assertEqual(obj.search('hello'), False)
        self.assertEqual(obj.search('hhllo'), True)
        self.assertEqual(obj.search('hell'), False)

    def test_lru_cache(self):
        cache = LRUCache(2)
        cache.put(1,1)
        cache.put(2,2)
        self.assertEqual(cache.get(1), 1)
        self.assertEqual(cache.get(2), 2)

if __name__ == '__main__':
    unittest.main()

