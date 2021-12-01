# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 递归方法
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 1
        elif root.left is not None and root.right is None:
            return 1 + self.minDepth(root.left)
        elif root.left is None and root.right is not None:
            return 1 + self.minDepth(root.right)
        else:
            return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
