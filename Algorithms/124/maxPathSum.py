# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -99999999
        self.get_max(root)
        return self.ans

    def get_max(self, root):
        if not root:
            return 0
        left_max = max(0, self.get_max(root.left))
        right_max = max(0, self.get_max(root.right))
        self.ans = max(self.ans, root.val + left_max + right_max)
        return root.val + max(left_max, right_max)
