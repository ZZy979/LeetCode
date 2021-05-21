# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = deque([(root, 0, None)])
        dx = dy = -1
        px = py = None
        while q and (dx == -1 or dy == -1):
            node, depth, parent = q.popleft()
            if node.val == x:
                dx, px = depth, parent
            elif node.val == y:
                dy, py = depth, parent
            if node.left:
                q.append((node.left, depth + 1, node))
            if node.right:
                q.append((node.right, depth + 1, node))
        return dx == dy and px is not py
