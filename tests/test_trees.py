import copy
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

        self.tree5 = Tree()
        self.tree5.root = TreeNode(1)
        self.tree5.root.left = TreeNode(2)
        self.tree5.root.right = TreeNode(2)
        self.tree5.root.left.left = TreeNode(3)
        self.tree5.root.left.right = TreeNode(4)
        self.tree5.root.right.left = TreeNode(4)
        self.tree5.root.right.right = TreeNode(3)

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


    def test_symmetric(self):
        self.assertEqual(is_symmetric(self.tree2.root), False)
        self.assertEqual(is_symmetric(self.tree5.root), True)
        self.assertEqual(is_symmetric_iterative(self.tree5.root), True)

    def test_same(self):
        self.assertEqual(same_tree(self.tree1.root, self.tree1.root), True)
        self.assertEqual(same_tree(self.tree2.root, self.tree2.root), True)
        self.assertEqual(same_tree(self.tree3.root, self.tree3.root), True)
        self.assertEqual(same_tree(self.tree4.root, self.tree4.root), True)
        self.assertEqual(same_tree(self.tree5.root, self.tree5.root), True)
        self.assertEqual(same_tree(self.tree5.root, self.tree1.root), False)
        self.assertEqual(same_tree(self.tree4.root, self.tree2.root), False)
        self.assertEqual(same_tree(self.tree3.root, self.tree3.root), True)
        self.assertEqual(same_tree(self.tree2.root, self.tree4.root), False)
        self.assertEqual(same_tree(self.tree1.root, self.tree5.root), False)
        self.assertEqual(same_tree(self.tree5.root, self.tree4.root), False)
        self.assertEqual(same_tree(self.tree5.root, self.tree3.root), False)
        self.assertEqual(same_tree(self.tree5.root, self.tree2.root), False)

    def test_max_depth(self):
        tree1 = Tree()
        tree2 = Tree()
        tree2.root = TreeNode(1)
        self.assertEqual(max_depth(self.tree1.root), 3)
        self.assertEqual(max_depth(self.tree2.root), 3)
        self.assertEqual(max_depth(self.tree3.root), 3)
        self.assertEqual(max_depth(self.tree4.root), 3)
        self.assertEqual(max_depth(self.tree5.root), 3)
        self.assertEqual(max_depth(tree1.root), 0)
        self.assertEqual(max_depth(tree2.root), 1)
        self.assertEqual(max_depth_v2(self.tree1.root), 3)
        self.assertEqual(max_depth_v2(self.tree2.root), 3)
        self.assertEqual(max_depth_v2(self.tree3.root), 3)
        self.assertEqual(max_depth_v2(self.tree4.root), 3)
        self.assertEqual(max_depth_v2(self.tree5.root), 3)
        self.assertEqual(max_depth_v2(tree1.root), 0)
        self.assertEqual(max_depth_v2(tree2.root), 1)

    def test_min_depth(self):
        self.assertEqual(min_depth(self.tree1.root), 3)
        self.assertEqual(min_depth(self.tree4.root), 2)


    def test_build_inpre(self):
        self.assertEqual(inorder_recursive(build_tree_inpre([3,9,20,15,7],[9,3,15,20,7])), 
                         '9,3,15,20,7')

    def test_build_post(self):
        self.assertEqual(inorder_recursive(build_tree_postorder([9,3,15,20,7],[9,15,7,20,3])),
                         '9,3,15,20,7')

    def test_invert_tree(self):
        self.assertEqual(inorder_recursive(invert_tree(self.tree2.root)), '7,3,6,1,5,2,4')

    def test_average_levels(self):
        self.assertEqual(average_levels(self.tree1.root), [50,55,48.75])

    def test_max_levels(self):
        self.assertEqual(max_levels(self.tree1.root), [50, 100, 110])

    def test_array_bst(self):
        self.assertEqual(inorder_recursive(array_bst([-10,-3,0,5,9])), '-10,-3,0,5,9')
        self.assertEqual(inorder_recursive(array_bst_v2([-10,-3,0,5,9])), '-10,-3,0,5,9')

    def test_is_balanced(self):
        self.assertEqual(is_balanced(self.tree1.root), True)

    def test_path_sum(self):
        self.assertEqual(path_sum(self.tree1.root, 65), True)

    def test_path_sums_two(self):
        self.assertEqual(path_sums_all(self.tree1.root, 65), [[50, 10, 5]])

    def test_sum_path(self):
        root = TreeNode(4)
        root.left = TreeNode(9)
        root.right = TreeNode(0)
        root.left.left = TreeNode(5)
        root.left.right = TreeNode(1)

        root1 = TreeNode(1)
        root1.left = TreeNode(2)
        root1.right = TreeNode(3)

        self.assertEqual(sum_paths(root), 1026)
        self.assertEqual(sum_paths(root1), 25)

    def test_paths(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.right = TreeNode(5)

        self.assertEqual(tree_paths(root), [[1,2,5], [1,3]])

    def test_merge_trees(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root1 = TreeNode(4)
        root1.left = TreeNode(5)
        root1.right = TreeNode(6)
        self.assertEqual(inorder_recursive(merge_two_trees(root, root1)), '7,5,9')

    def test_sum_leaf(self):
        self.assertEqual(sum_left_leaves(self.tree4.root), 24)
        self.assertEqual(sum_left_leaves_v2(self.tree4.root), 24)

    def test_flatten(self):
        root = copy.deepcopy(self.tree1.root)
        flatten(root)
        self.assertEqual(inorder_recursive(root), '50,10,5,20,100,60,110')

if __name__ == '__main__':
    unittest.main()