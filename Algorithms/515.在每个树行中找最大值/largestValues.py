# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            level_max = -0x80000000
            for _ in range(len(q)):
                node = q.popleft()
                level_max = max(level_max, node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(level_max)
        return ans
