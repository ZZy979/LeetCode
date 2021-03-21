# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return balanced(root)[0]


def balanced(root):
    if not root:
        return True, 0
    lb, lh = balanced(root.left)
    rb, rh = balanced(root.right)
    return lb and rb and abs(lh - rh) <= 1, 1 + max(lh, rh)
