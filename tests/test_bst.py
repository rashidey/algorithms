from algorithms.bst import *

import unittest

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

def convert_to_list(A):
    dummy = newList = Node(0)
    for number in A:
        dummy.next = Node(number)
        dummy = dummy.next
    return newList.next

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

    def test_delete_node(self):
        bst1 = BST()
        bst1.root = TreeNode(1)
        bst1.root.left = TreeNode(2)
        bst1.root.right = TreeNode(3)
        self.assertEqual(str(bst1), '2,1,3')
        bst1.root = delete_node(bst1.root, 1)
        self.assertEqual(str(bst1), '2,3')

    def test_is_valid(self):
        bst1 = BST()
        bst1.root = TreeNode(2)
        bst1.root.left = TreeNode(1)
        bst1.root.right = TreeNode(3)
        bst2 = BST()
        bst2.root = TreeNode(1)
        bst2.root.left = TreeNode(1)

        self.assertEqual(is_valid_bst(bst1.root), True)
        self.assertEqual(is_valid_bst(bst2.root), False)
        self.assertEqual(is_valid_bst_v2(bst1.root), True)
        self.assertEqual(is_valid_bst_v2(bst2.root), False)

    def test_sorted_list_bst(self):
        list1 = convert_to_list([-10,-3,0,5,9])
        test = BST()
        test.root = sorted_list_bst(list1)
        self.assertEqual(str(test), '-10,-3,0,5,9')

    def test_increasing_bst(self):
        list1 = BST()
        list1.insert_bst(5)
        list1.insert_bst(3)
        list1.insert_bst(6)
        list1.insert_bst(2)
        list1.insert_bst(4)
        list1.insert_bst(8)
        list1.insert_bst(1)
        list1.insert_bst(7)
        list1.insert_bst(9)
        list1.root = increasing_bst(list1.root)
        self.assertEqual(str(list1), '1,2,3,4,5,6,7,8,9')

if __name__ == '__main__':
    unittest.main()
