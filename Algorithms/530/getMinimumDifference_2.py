# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 官方题解：中序遍历
class Solution:

    def __init__(self):
        self.ans = 0x7fffffff
        self.pre = -1
    
    def getMinimumDifference(self, root: TreeNode) -> int:
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
