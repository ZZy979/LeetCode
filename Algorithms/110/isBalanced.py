# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.height_and_balanced(root)[1]
    
    def height_and_balanced(self, root):
        if root is None:
            return 0, True
        else:
            lh, lb = self.height_and_balanced(root.left)
            rh, rb = self.height_and_balanced(root.right)
            return 1 + max(lh, rh), lb and rb and abs(lh - rh) <= 1
