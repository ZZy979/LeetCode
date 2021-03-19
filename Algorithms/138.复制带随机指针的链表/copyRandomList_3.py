"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

# 官方题解3：修改原始链表，1->2->3 => 1->1'->2->2'->3->3'
# 时间复杂度O(n)，空间复杂度O(1)
# 44 ms
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return None
        p = head
        while p:
            p.next = Node(p.val, p.next)
            p = p.next.next
        
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        
        new_head = head.next
        p_old, p_new = head, head.next
        while p_new.next:
            p_old.next = p_old = p_old.next.next
            p_new.next = p_new = p_new.next.next
        return new_head
