"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        
        p = head
        while True:
            if p.val < insertVal <= p.next.val:
                p.next = Node(insertVal, p.next)
                return head
            p = p.next
            if p is head:
                break
        
        p = head
        while p.next is not head and p.next.val >= p.val:
            p = p.next
        p.next = Node(insertVal, p.next)
        return head
