# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        self.vals = set()
        self.k = k
        return self.preorder(root)
    
    def preorder(self, root):
        if not root:
            return False
        if self.k - root.val in self.vals:
            return True
        self.vals.add(root.val)
        return self.preorder(root.left) or self.preorder(root.right)
