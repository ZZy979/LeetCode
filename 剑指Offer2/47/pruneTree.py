# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return root if prune(root) else None


def prune(root):
    if not root:
        return False
    left, right = prune(root.left), prune(root.right)
    if not left:
        root.left = None
    if not right:
        root.right = None
    return left or right or root.val == 1
