# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def __init__(self):
        self.pre = None
    
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if root is None:
            return None
        suc = self.inorderSuccessor(root.left, p)
        if suc is not None:
            return suc
        if self.pre == p.val:
            return root
        self.pre = root.val
        return self.inorderSuccessor(root.right, p)
