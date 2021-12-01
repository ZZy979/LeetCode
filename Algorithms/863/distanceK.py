# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.ans = []
        self.dfs(root, target.val, k)
        return self.ans
    
    def dfs(self, root, target, k):
        if not root:
            return -1
        if root.val == target:
            self.bfs(root, k)
            return 1
        dl = self.dfs(root.left, target, k)
        if dl > 0:
            if dl == k:
                self.ans.append(root.val)
            else:
                self.bfs(root.right, k - dl - 1)
            return dl + 1
        dr = self.dfs(root.right, target, k)
        if dr > 0:
            if dr == k:
                self.ans.append(root.val)
            else:
                self.bfs(root.left, k - dr - 1)
            return dr + 1
        return -1
    
    def bfs(self, root, k):
        if not root or k < 0:
            return
        q = deque([root])
        for _ in range(k):
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        self.ans.extend(node.val for node in q)
