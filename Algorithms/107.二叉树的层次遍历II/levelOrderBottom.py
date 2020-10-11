# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        ans = []
        q = deque()
        cur_layer = 0
        if root is not None:
            q.append((root, 0))
        while q:
            layer_res = []
            while q and q[0][1] == cur_layer:
                n, l = q.popleft()
                layer_res.append(n.val)
                if n.left is not None:
                    q.append((n.left, l + 1))
                if n.right is not None:
                    q.append((n.right, l + 1))
            ans.append(layer_res)
            cur_layer += 1
        return list(reversed(ans))
