"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

# 方法1：递归
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        if not root:
            return
        for child in root.children:
            yield from self.postorder(child)
        yield root.val
