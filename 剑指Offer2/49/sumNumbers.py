# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.path_sum(root, 0)

    def path_sum(self, root, path_val):
        if not root:
            return 0
        path_val = path_val * 10 + root.val
        if not root.left and not root.right:
            return path_val
        else:
            return self.path_sum(root.left, path_val) + self.path_sum(root.right, path_val)
