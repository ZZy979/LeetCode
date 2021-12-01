# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 直接DFS，时间复杂度O(n)，空间复杂度O(log n)
# 92 ms
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)
