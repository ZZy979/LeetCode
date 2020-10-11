# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rob(self, root: TreeNode) -> int:
        self.res = {}
        return max(self.rob_rec(root, True), self.rob_rec(root, False))
    
    def rob_rec(self, root, rob_root):
        if root is None:
            return 0
        elif rob_root:
            if root not in self.res:
                self.res[root] = root.val + self.rob_rec(root.left, False) + self.rob_rec(root.right, False)
            return self.res[root]
        else:
            return max(self.rob_rec(root.left, True), self.rob_rec(root.left, False)) + max(self.rob_rec(root.right, True), self.rob_rec(root.right, False))
