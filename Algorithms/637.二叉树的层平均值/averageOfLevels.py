# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        if not root:
            return []
        ans = []
        q = deque([(root, 0)])
        cur_depth = 0
        level_sum = 0
        level_count = 0
        while q:
            n, level = q.popleft()
            if level > cur_depth:
                ans.append(level_sum / level_count)
                level_sum = level_count = 0
                cur_depth = level
            level_sum += n.val
            level_count += 1
            if n.left:
                q.append((n.left, cur_depth + 1))
            if n.right:
                q.append((n.right, cur_depth + 1))
        ans.append(level_sum / level_count)
        return ans
