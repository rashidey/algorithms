from algorithms.bst import *

import unittest

class TestBST(unittest.TestCase):
    def testBST(self):
        #BST Node
        bst1 = BST()
        bst1.root = TreeNode(6)
        bst1.root.left = TreeNode(4)
        bst1.root.right = TreeNode(8)
        bst1.root.left.left = TreeNode(2)
        bst1.root.left.right = TreeNode(5)
        
        #Search
        self.assertEqual(bst1.search(3), False)
        self.assertEqual(bst1.search(4), True)
        self.assertEqual(bst1.search(12), False)

        #BST Insert
        bst2 = BST()
        bst2.insert_bst(20)
        bst2.insert_bst(10)
        bst2.insert_bst(30)
        bst2.insert_bst(15)
        self.assertEqual(str(bst2), '10,15,20,30')

        #BST CountV2
        bst3 = BST()
        bst4 = BST()
        bst4.insert_bst(0)

        self.assertEqual(bst2.count_v2(), 4)
        self.assertEqual(bst1.count_v2(), 5)
        self.assertEqual(bst1.count_v2(), 5)
        self.assertEqual(bst3.count_v2(), 0)
        self.assertEqual(bst4.count_v2(), 1)
        self.assertEqual(bst2.count_v3(), 4)
        self.assertEqual(bst1.count_v3(), 5)
        self.assertEqual(bst1.count_v3(), 5)
        self.assertEqual(bst3.count_v3(), 0)
        self.assertEqual(bst4.count_v3(), 1)

        #Get Max
        self.assertEqual(bst1.get_max(), 8)
        self.assertEqual(bst2.get_max(), 30)
        self.assertEqual(bst3.get_max(), None)
        self.assertEqual(bst4.get_max(), 0)

        #Get Min
        self.assertEqual(bst1.get_min(), 2)
        self.assertEqual(bst2.get_min(), 10)
        self.assertEqual(bst3.get_min(), None)
        self.assertEqual(bst4.get_min(), 0)

        #Get height
        self.assertEqual(bst1.get_height(), 3)
        self.assertEqual(bst2.get_height(), 3)
        self.assertEqual(bst3.get_height(), 0)
        self.assertEqual(bst4.get_height(), 1)

        #Delete Node
        bst1.delete_node(6)
        bst2.delete_node(10)
        bst2.delete_node(32)
        bst4.delete_node(0)
        self.assertEqual(str(bst1), '2,4,5,8')
        self.assertEqual(str(bst2), '15,20,30')
        self.assertEqual(str(bst4), '')

class TestBSTFunctions(unittest.TestCase):
    def test_recover_tree(self):
        bst1 = BST()
        bst1.root = TreeNode(1)
        bst1.root.left = TreeNode(3)
        bst1.root.left.right = TreeNode(2)
        recover_tree(bst1.root)
        self.assertEqual('1,2,3', str(bst1))

        
if __name__ == '__main__':
    unittest.main()
