# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        self.ans = 0x7fffffff
        self.pre = -1
        self.inorder(root)
        return self.ans
    
    def inorder(self, root):
        if not root:
            return
        self.inorder(root.left)
        if self.pre != -1:
            self.ans = min(self.ans, root.val - self.pre)
        self.pre = root.val
        self.inorder(root.right)
