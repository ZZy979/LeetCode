# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        level = 0
        while q:
            prev = 0 if level % 2 == 0 else 0x7fffffff
            for i in range(len(q)):
                node = q.popleft()
                if node.val % 2 == level % 2 or level % 2 == 0 and node.val <= prev or level % 2 == 1 and node.val >= prev:
                    return False
                prev = node.val
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
