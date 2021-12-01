"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        ans = self.cur = Node(0, None, None, None)
        self.dfs(head)
        ans.next.prev = None
        return ans.next
    
    def dfs(self, head):
        p = head
        while p:
            self.cur.next = Node(p.val, self.cur, None, None)
            self.cur = self.cur.next
            if p.child:
                self.dfs(p.child)
            p = p.next
