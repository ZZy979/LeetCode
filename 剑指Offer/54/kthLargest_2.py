# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        self.count = k
        self.inorder(root)
        return self.ans
    
    def inorder(self, root):
        if root.right:
            self.inorder(root.right)
        self.count -= 1
        if self.count == 0:
            self.ans = root.val
            return
        if root.left:
            self.inorder(root.left)
