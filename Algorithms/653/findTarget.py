# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.vals = set()

    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        if k - root.val in self.vals:
            return True
        self.vals.add(root.val)
        return self.findTarget(root.left, k) or self.findTarget(root.right, k)
