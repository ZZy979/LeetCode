# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict

class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        stack = [(root, 0, 0)]
        d = defaultdict(list)
        while stack:
            node, row, col = stack.pop()
            if node:
                d[col].append((row, node.val))
                stack.append((node.left, row + 1, col - 1))
                stack.append((node.right, row + 1, col + 1))
        return [[val for _, val in sorted(d[col])] for col in sorted(d)]
