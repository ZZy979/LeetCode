# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        return max(self.rob_rec(root))
    
    def rob_rec(self, root):
        if root is None:
            return 0, 0
        left = self.rob_rec(root.left)
        right = self.rob_rec(root.right)
        return max(left) + max(right), root.val + left[0] + right[0]
