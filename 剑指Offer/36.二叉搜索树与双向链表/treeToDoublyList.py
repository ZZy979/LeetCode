"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None
        self.head = self.prev = None
        self.convert(root)
        self.head.left, self.prev.right = self.prev, self.head
        return self.head
    
    def convert(self, root):
        if not root:
            return
        self.convert(root.left)
        if not self.head:
            self.head = root
        else:
            root.left, self.prev.right = self.prev, root
        self.prev = root
        self.convert(root.right)
