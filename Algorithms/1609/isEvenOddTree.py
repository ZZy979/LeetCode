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
            if level % 2 == 0 and not (all(q[i].val % 2 == 1 for i in range(len(q))) and all(q[i].val < q[i + 1].val for i in range(len(q) - 1))) \
                or level % 2 == 1 and not (all(q[i].val % 2 == 0 for i in range(len(q))) and all(q[i].val > q[i + 1].val for i in range(len(q) - 1))):
                return False
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return True
