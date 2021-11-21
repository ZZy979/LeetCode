# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root)
        return self.ans
    
    def dfs(self, root):
        if not root:
            return 0
        left_sum, right_sum = self.dfs(root.left), self.dfs(root.right)
        self.ans += abs(left_sum - right_sum)
        return left_sum + right_sum + root.val
