# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        ans = []
        left2right = True
        while q:
            layer = deque()
            for i in range(len(q)):
                node = q.popleft()
                if left2right:
                    layer.append(node.val)
                else:
                    layer.appendleft(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(list(layer))
            left2right = not left2right
        return ans
