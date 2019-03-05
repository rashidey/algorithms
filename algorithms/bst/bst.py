class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def inorderUtil(self, root):
        if root:
            self.inorderUtil(root.left)
            print(root.val, end=' ')
            self.inorderUtil(root.right)
    def inorder(self):
        self.inorderUtil(self.root)
    