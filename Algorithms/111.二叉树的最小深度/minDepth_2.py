# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

# 层序遍历方法
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = deque()
        queue.append((root, 1))
        while deque:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))
