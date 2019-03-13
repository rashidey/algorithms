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


if __name__ == '__main__':
    unittest.main()

