# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        elif root.left is None and root.right is None:
            return root.val == sum
        else:
            return root.left is not None and self.hasPathSum(root.left, sum - root.val) \
                or root.right is not None and self.hasPathSum(root.right, sum - root.val)
