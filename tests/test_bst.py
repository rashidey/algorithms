from algorithms.bst import *

import unittest

class TestBST(unittest.TestCase):
    def test_bst(self):
        bst1 = BST()
        bst1.root = TreeNode(5)
        bst1.root.left = TreeNode(1)
        bst1.root.right = TreeNode(10)
        bst1.root.left.left = TreeNode(0)
        bst1.root.left.right = TreeNode(4)
        self.assertEqual('0 1 4 5 10 ', bst1.inorder())

    def test_recover_tree(self):
        bst1 = BST()
        bst1.root = TreeNode(1)
        bst1.root.left = TreeNode(3)
        bst1.root.left.right = TreeNode(2)
        recover_tree(bst1.root)
        result = bst1.inorder()
        self.assertEqual('1 2 3 ', result)

if __name__ == '__main__':
    unittest.main()
