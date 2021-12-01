# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import Counter

class Solution:
    def __init__(self):
        self.counter = Counter()
    
    def findMode(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        self.count(root)
        m = self.counter.most_common(1)[0][1]
        return [k for k, v in self.counter.items() if v == m]
    
    def count(self, root):
        if not root:
            return
        self.counter[root.val] += 1
        self.count(root.left)
        self.count(root.right)
