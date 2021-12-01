# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.search(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)

    def search(self, root, s):
        if not root:
            return 0
        s -= root.val
        return int(s == 0) + self.search(root.left, s) + self.search(root.right, s)
