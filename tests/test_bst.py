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

if __name__ == '__main__':
    from context import *
    unittest.main()
