# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# 官方题解
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.ans = -1
        self.root_val = root.val
        self.dfs(root)
        return self.ans

    def dfs(self, root):
        if not root:
            return
        if self.ans != -1 and root.val >= self.ans:
            return
        if root.val > self.root_val:
            self.ans = root.val
        self.dfs(root.left)
        self.dfs(root.right)
