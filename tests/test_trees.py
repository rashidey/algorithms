from algorithms.trees import *
import unittest

class TestSetup(unittest.TestCase):
    
    def setUp(self):
        self.tree1 = Tree()
        self.tree1.insert(50)
        self.tree1.insert(10)
        self.tree1.insert(100)
        self.tree1.insert(5)
        self.tree1.insert(20)
        self.tree1.insert(60)
        self.tree1.insert(110)

        self.tree2 = Tree()
        self.tree2.insert(1)
        self.tree2.insert(2)
        self.tree2.insert(3)
        self.tree2.insert(4)
        self.tree2.insert(5)
        self.tree2.insert(6)
        self.tree2.insert(7)

        self.tree3 = Tree()
        self.tree3.root = TreeNode(1)
        self.tree3.root.right = TreeNode(2)
        self.tree3.root.right.left = TreeNode(3)

        self.tree4 = Tree()
        self.tree4.root = TreeNode(3)
        self.tree4.root.left = TreeNode(9)
        self.tree4.root.right = TreeNode(20)
        self.tree4.root.right.left = TreeNode(15)
        self.tree4.root.right.right = TreeNode(7)

class TestTree(TestSetup):
    
    def test_tree(self):
        self.assertEqual(str(self.tree2), '1,2,3,4,5,6,7')
    
    def test_inorder(self):
        self.assertEqual(inorder_recursive(self.tree2.root), '4,2,5,1,6,3,7')
        
        self.assertEqual(self.tree1.root.val, 50)
        self.assertEqual(self.tree1.root.left.val, 10)
        self.assertEqual(self.tree1.root.right.val, 100)
        self.assertEqual(self.tree1.root.left.left.val, 5)
        self.assertEqual(self.tree1.root.left.right.val, 20)
        self.assertEqual(self.tree1.root.right.left.val, 60)
        self.assertEqual(self.tree1.root.right.right.val, 110)
        
        self.assertEqual(inorder_iterative(self.tree1.root), '5,10,20,50,60,100,110')
        self.assertEqual(inorder_recursive(self.tree1.root), '5,10,20,50,60,100,110')
        self.assertEqual(inorder_iterative(self.tree2.root), '4,2,5,1,6,3,7')

    def test_preorder(self):
        self.assertEqual(preorder_recursive(self.tree1.root), '50,10,5,20,100,60,110')
        self.assertEqual(preorder_recursive(self.tree2.root), '1,2,4,5,3,6,7')
        self.assertEqual(preorder_recursive(self.tree3.root), '1,2,3')
        self.assertEqual(preorder_iterative(self.tree1.root), '50,10,5,20,100,60,110')
        self.assertEqual(preorder_iterative(self.tree2.root), '1,2,4,5,3,6,7')
        self.assertEqual(preorder_iterative(self.tree3.root), '1,2,3')

    def test_postorder(self):
        self.assertEqual(postorder_recursive(self.tree2.root), '4,5,2,6,7,3,1')
        self.assertEqual(postorder_iterative(self.tree2.root), '4,5,2,6,7,3,1')

    def test_level_order(self):
        self.assertEqual(level_order_one(self.tree4.root), [[3],[9,20],[15,7]])
        self.assertEqual(level_order_two(self.tree4.root), [[15,7],[9,20],[3]])
        self.assertEqual(zigzag_level_order(self.tree4.root), [[3],[20,9],[15,7]])




if __name__ == '__main__':
    unittest.main()