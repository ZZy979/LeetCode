"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

# 非递归版本
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        cur_root = root
        while cur_root.left:
            next_root = cur_root.left
            while cur_root.next:
                cur_root.left.next = cur_root.right
                cur_root.right.next = cur_root.next.left
                cur_root = cur_root.next
            cur_root.left.next = cur_root.right
            cur_root = next_root
        return root
