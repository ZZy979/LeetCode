# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.node1 = self.node2 = self.pre = None

    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.inorder(root)
        self.node1.val, self.node2.val = self.node2.val, self.node1.val
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre and self.pre.val > root.val:
            if not self.node1:
                self.node1 = self.pre
            self.node2 = root
        self.pre = root
        self.inorder(root.right)
