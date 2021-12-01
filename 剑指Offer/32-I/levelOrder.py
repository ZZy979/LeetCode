# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        q = deque([root])
        ans = []
        while q:
            node = q.popleft()
            ans.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return ans
