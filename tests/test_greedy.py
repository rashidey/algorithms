from algorithms.greedy import *
import unittest

class TestSuite(unittest.TestCase):
    def test_queue_height(self):
        values = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]] 
        out = [[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
        self.assertEqual(reconstruct_queue(values), out)

    def test_sub_seq(self):
        self.assertEqual(is_subsequence('abc', 'ahbgdc'), True)
    
    def test_min_arrows(self):
        self.assertEqual(min_arrows([[10,16], [2,8], [1,6], [7,12]]), 2)

    def test_stones(self):
        self.assertEqual(moving_stones(1,2,5),[1,2])

    def test_senate(self):
        self.assertEqual(predict_victory('RDD'), 'Dire')

    def test_make_paran(self):
        self.assertEqual(make_paran_valid('(()))'), 1)

    def test_erase(self):
        self.assertEqual(erase_overlap([[1,2],[2,3],[3,4],[1,3]]), 1)

    def test_reorganize(self):
        self.assertEqual(reorganize_string('aab'), 'aba')