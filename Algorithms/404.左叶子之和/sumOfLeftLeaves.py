# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        return self.sum_of_left_leaves_rec(root, None)
    
    def sum_of_left_leaves_rec(self, root, parent):
        if not root:
            return 0
        elif not root.left and not root.right:
            return root.val if parent and root is parent.left else 0
        else:
            return self.sum_of_left_leaves_rec(root.left, root) + self.sum_of_left_leaves_rec(root.right, root)
